from dataclasses import dataclass
from fastapi.responses import JSONResponse

from fastapi import HTTPException
from reflex.components.el import Details
from sqlalchemy.orm import Session
import cv2

from spot.backend.app.crud.crud_tracks import TracksDB
from ..schemas.tracks import CreateTracksSchema, GetTracksSchema
from ..utils.aws.get_bucket import s3_client, bucket_name
from ..utils.aws.logger import logger

@dataclass
class TracksRepositories:
    db: Session 

    def create_tracks(self,track: CreateTracksSchema):
        try:
            video = cv2.VideoCapture(track.location_url)
            total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = video.get(cv2.CAP_PROP_FPS)
            duration = int(total_frames / fps)
            video.release()

            s3_client.head_object(Bucket=bucket_name, Key=track.title)

            # Añadir parámetros para controlar el comportamiento de la descarga
            url = s3_client.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": bucket_name,
                    "Key": track.title,
                    "ResponseContentType": "audio/mp3",  # Ajusta según el tipo de video
                    "ResponseContentDisposition": "inline",  # Esto evita la descarga automática
                },
                ExpiresIn=172800,  # URL válida por 2 días
                HttpMethod="GET",
            )
            print(url)

            s3_client.upload_file(track.location_url, bucket_name, track.title)
            return TracksDB(self.db).create_tracks(track, duration, url)

        except HTTPException as he:
            raise HTTPException(status_code=500, detail=str(he))
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_tracks(self, skip:int , limit:int):
        try:
            return TracksDB(self.db).get_tracks(skip,limit)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_info_tracks(self, track_id:int):
        try:
            return TracksDB(self.db).get_info_tracks(track_id) 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

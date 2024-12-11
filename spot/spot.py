"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from spot.services import APIClient 

playlist_data = APIClient().get_tracks()

class State(rx.State):
    image_src: str = ""
    song_title: str = "" 
    artist_name: str = ""
    url_song = str = ""

    @rx.event
    def update_song(self, item):
        self.image_src = item["image"]
        self.song_title =item["title"] 
        self.artist_name = item["name"] 
        self.url_song = item["s3_bucket_url"] 

def create_icon(icon_tag):
    """Create an icon with specified tag and styling."""
    return rx.icon(
        tag=icon_tag,
        height="1.25rem",
        margin_right="0.75rem",
        width="1.25rem",
    )


def create_nav_link(icon_tag, link_text):
    """Create a navigation link with an icon and text."""
    return rx.el.a(
        create_icon(icon_tag=icon_tag), link_text, href="#",
        display="flex",
        _hover={"color": "#ffffff"},
        align_items="center",
        color="#D1D5DB",
    )


def create_nav_item(icon_tag, item_text):
    """Create a navigation item with an icon and text."""
    return rx.el.li(create_nav_link(icon_tag=icon_tag, link_text=item_text))


def create_section_heading(heading_text):
    """Create a section heading with specified text and styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.5rem",
        line_height="2rem",
        as_="h3",
    )


def create_playlist_image(alt_text, image_src):
    """Create an image for a playlist with specified alt text and source."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height="10rem",
        margin_bottom="0.5rem",
        object_fit="cover",
        border_radius="0.375rem",
        width="100%",
    )


def create_subtitle(subtitle_text):
    """Create a subtitle with specified text and styling."""
    return rx.heading(subtitle_text, font_weight="600", as_="h4", size="3")


def create_artist(artist_text):
    """Create a description text with specified content and styling."""
    return rx.text(
        artist_text,
        color="#9CA3AF",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_playlist_card(item):
    """Create a playlist card with image, title, and description."""
    return rx.box(
        create_playlist_image(alt_text=item["title"], image_src=item["image"]),
        create_subtitle(subtitle_text=item["title"]),
        create_artist(artist_text=item["name"]),
        rx.icon(
            tag="play",
            background_color="#7C3AED",
            cursor="pointer",
            height="2rem",
            _hover={"background-color": "#6D28D9"},
            padding="0.25rem",
            border_radius="9999px",
            color="#ffffff",
            width="2rem",
            on_click= lambda: State.update_song(item)
        ),
        background_color="#1F2937",
        padding="1rem",
        border_radius="0.5rem",
    )


def create_album_cover(alt_text, image_height, image_src, image_width):
    """Create an album cover image with specified dimensions and source."""
    return rx.image(
        src=image_src,
        alt=alt_text,
        height=image_height,
        margin_right="1rem",
        object_fit="cover",
        border_radius="0.375rem",
        width=image_width,
    )


def create_song_info(song_title, artist_name):
    """Create a box containing song title and artist information."""
    return rx.box(
        create_subtitle(subtitle_text=song_title),
        create_artist(artist_text=artist_name),
    )


def create_action_icon(icon_tag, item ):
    """Create an interactive icon for actions like play, pause, etc."""
    return rx.icon(
        tag=icon_tag,
        cursor="pointer",
        height="1.25rem",
        _hover={"color": "#ffffff"},
        color="#9CA3AF",
        width="1.25rem",
        on_click=lambda: State.update_song(item)
    )


def create_song_actions(item):
    """Create a set of action icons for song interaction."""
    return rx.flex(
        create_action_icon(icon_tag="heart", item=None),
        create_action_icon(icon_tag="play",item=item),
        class_name="ml-auto",
        display="flex",
        align_items="center",
        column_gap="1rem",
    )


def create_recently_played_item(item):
    """Create a recently played item with album cover, song info, and actions."""
    return rx.flex(
        create_album_cover(
            alt_text=item["title"],
            image_height="4rem",
            image_src=item["image"],
            image_width="4rem",
        ),
        create_song_info(song_title=item["title"], artist_name=item["name"]),
        create_song_actions(item),
        background_color="#1F2937",
        display="flex",
        align_items="center",
        padding="1rem",
        border_radius="0.5rem",
    )

def create_sidebar():
    """Create the sidebar containing logo and navigation items."""
    return rx.box(
        rx.box(
        #     rx.heading(
        #         "Spot",
        #         font_weight="700",
        #         font_size="1.875rem",
        #         line_height="2.25rem",
        #         color="#8B5CF6",
        #         as_="h1",
        #     ),
        #     margin_bottom="2rem",
        # ),
        # rx.list(  # type: ignore
        #     # create_nav_item(icon_tag="<House />", item_text=" Menu "),
        #     # create_nav_item(icon_tag="search", item_text=" Buscador "),
        #     # create_nav_item(
        #     #     icon_tag="library",
        #     #     item_text=" Mi biblioteca ",
        #     # ),
        #     # create_nav_item(
        #     #     icon_tag="plus",
        #     #     item_text=" Crear lista de reproduccion ",
        #     # ),
        #     # create_nav_item(icon_tag="heart", item_text=" Me gusta "),
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
        background_color="#1F2937",
        padding="1.5rem",
        width="16rem",
    )


def create_hero_section():
    """Create the hero section with 'Discover Weekly' heading and description."""
    return rx.box(
        rx.heading(
            "Spot",
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            as_="h2",
        ),
        rx.text(
            "Tu playlist personal, actualizada todos los dias",
            # "Your personal playlist, updated every Monday",
            color="#D1D5DB",
        ),
        class_name="bg-gradient-to-r from-purple-800 to-indigo-800",
        padding="1.5rem",
    )


def create_featured_playlists():
    """Create the featured playlists section with multiple playlist cards."""
    return rx.box(
        create_section_heading(heading_text="Featured Playlists"),
        rx.box(
            *[
                create_playlist_card(item)
                for item in playlist_data #type: ignore
            ],
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(2, minmax(0, 1fr))",
                    "640px": "repeat(3, minmax(0, 1fr))",
                    "768px": "repeat(4, minmax(0, 1fr))",
                    "1024px": "repeat(5, minmax(0, 1fr))",
                }
            ),
        ),
        padding="1.5rem",
    )


def create_main_content():
    """Create the main content area including hero, featured playlists, and recently played."""
    return rx.box(
        create_hero_section(),
        create_featured_playlists(),
        rx.box(
            create_section_heading(heading_text="Recently Played"),
            rx.box(
                *[
                    create_recently_played_item(item)
                    for item in playlist_data #type: ignore
                ],
                display="flex",
                flex_direction="column",
                gap="1rem",
            ),
            padding="1.5rem",
        ),
        flex="1 1 0%",
        overflow_y="auto",
    )


def create_playback_controls():
    """Create playback control buttons (previous, play/pause, next)."""
    return rx.flex(
        create_action_icon(icon_tag="skip-back", item=None ),
        rx.icon(
            tag="play",
            background_color="#7C3AED",
            cursor="pointer",
            height="2rem",
            _hover={"background-color": "#6D28D9"},
            padding="0.25rem",
            border_radius="9999px",
            color="#ffffff",
            width="2rem",
        ),
        create_action_icon(icon_tag="skip-forward", item=None),
        display="flex",
        align_items="center",
        column_gap="1rem",
    )


def create_player_bar():
    """Create the player bar with current song info, playback controls, and volume/fullscreen buttons."""
    return rx.flex(
        rx.flex(
            create_album_cover(
                alt_text=State.song_title,
                image_height="3.5rem",
                image_src=State.image_src,
                image_width="3.5rem",
            ),
            create_song_info(
                song_title=State.song_title,
                artist_name=State.artist_name,
            ),
            display="flex",
            align_items="center",
        ),
        rx.flex(
            rx.audio(
                url=State.url_song,
                height="32px",
            ),
            display="flex",
            align_items="center",
        ),     
        rx.flex(),
        display="flex",
        align_items="center",
        justify_content="space-between",
    )


def create_main_layout():
    """Create the main layout of the application including sidebar, main content, and player bar."""
    return rx.box(
        rx.flex(
            create_sidebar(),
            create_main_content(),
            display="flex",
            height="100vh",
        ),
        rx.box(
            create_player_bar(),
            background_color="#1F2937",
            border_color="#374151",
            border_top_width="1px",
            padding="1rem",
        ),
        background_color="#111827",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        color="#ffffff",
    )



def create_app():
    """Create the entire application including styles and main layout."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        create_main_layout(),

    )


def index() -> rx.Component:
    return create_app()


app = rx.App(theme=rx.theme(color_mode="light"))
app.add_page(index)

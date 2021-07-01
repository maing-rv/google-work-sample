"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._is_playing = False
        self._video_playing = 'None'
        self._is_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos: ")
        all_videos = self._video_library._videos
        for x in sorted(all_videos):
            tag_str = ' '.join(self._video_library.get_video(x)._tags)
            print(f'{self._video_library.get_video(x)._title} ({self._video_library.get_video(x)._video_id}) [{tag_str}]')
        #all_videos = self._video_library.get_all_videos()
        #for vid in all_videos:
            #tag_str = ' '.join(vid.tags)
            #print(f'{vid.title} ({vid.video_id}) [{tag_str}]') # not in alphabetical order, can turn into a list, then sorted

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        try:
            video = self._video_library.get_video(video_id) #._title
            if self._is_playing or self._is_paused: 
               print(f'Stopping video: {self._video_playing._title}')
               print(f'Playing video: {video._title}')
            #elif self._is_paused:
               #print(f'Stopping video: {self._video_playing._title}')
               #print(f'Playing video: {video._title}')
            else:
               print(f'Playing video: {video._title}')
               self._is_playing = True
        except AttributeError:
            print('Cannot play video: Video does not exist')
        self._is_paused = False
        self._video_playing = video
   
    def stop_video(self):
        """Stops the current video."""
        if self._is_playing:
            print(f'Stopping video: {self._video_playing._title}')
            self._is_playing = False
        else:
            print('Cannot stop video: No video is currently playing')
        self._video_playing = 'None'
        self._is_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        random_video = random.choice(all_videos)
        if self._is_playing:
            print(f'Stopping video: {self._video_playing._title}')
            print(f'Playing video: {random_video._title}')
        else:
            print(f'Playing video: {random_video._title}')
        self._video_playing = random_video
        self._is_playing = True
        #print('No videos available')

    def pause_video(self):
        """Pauses the current video."""
        if self._is_paused: 
            print(f'Video already paused: {self._video_playing._title}')
        elif self._is_playing:
            print(f'Pausing video: {self._video_playing._title}')
            self._is_paused = True
        elif not self._is_playing:
            print('Cannot pause video: No video is currently playing')

    def continue_video(self):
        """Resumes playing the current video."""
        if not self._is_playing:
            print('Cannot continue video: No video is currently playing')
        elif self._is_paused:
            print(f'Continuing video: {self._video_playing._title}')
            self._is_paused = False
            self._is_playing = True
        elif not self._is_paused:
            print('Cannot continue video: Video is not paused') 

    def show_playing(self):
        """Displays video currently playing."""
        if self._is_playing and not self._is_paused:
            print(f"Currently playing: {self._video_playing._title} ({self._video_playing._video_id}) [{' '.join(self._video_playing._tags)}]")
        elif self._is_playing and self._is_paused:
            print(f"Currently playing: {self._video_playing._title} ({self._video_playing._video_id}) [{' '.join(self._video_playing._tags)}] - PAUSED")
        else:
            print('No video is currently playing')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

import vlc

class VlcPlayer:
    def __init__(self, *args):
        if args:
            instance = vlc.instance(*args)
            self.media = instance.media_player_new()
        else:
            self.media = vlc.MediaPlayer()

    def set_uri(self, mrl):
        self.media.set_mrl(mrl)

    def play(self, path=None):
        if path:
            self.set_uri(path)
            return self.media.play()
        else:
            return self.media.play()

    def pause(self):
        self.media.pause()

    def resume(self):
        self.media.set_pause(0)

    def stop(self):
        self.media.stop()

    def release(self):
        return self.media.release()

    def is_playing(self):
        return self.media.is_playing()

    def get_time(self):
        return self.media.get_time()

    def set_time(self, ms):
        return self.media.set_time(ms)

    def get_length(self):
        return self.media.get_length()

    def get_volume(self):
        return self.media.audio_get_volume()

    def set_volume(self, vol):
        return self.media.audio_set_volume(vol)

    def get_state(self):
        state = self.media.get_state()
        if state == vlc.State.Playing:
            return 1
        elif state == vlc.State.Paused:
            return 0
        else:
            return -1
            
    def get_position(self):
        return self.media.get_position()

    def set_position(self, position):
        return self.media.set_position(position)

    def add_callback(self, event_type, callback):
        self.media.event_manager().event_attach(event_type, callback)

    def add_callback_time(self, event_type, callback):
        self.media.event_manager().event_attach(event_type, callback, self.media)

    def remove_callback(self, event_type, callback):
        self.media.event_manager().event_detach(event_type, callback)


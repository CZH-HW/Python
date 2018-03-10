class Gamestats():
    """Initialize the data of game stats"""
    def __init__(self, ai_settings):
        """Initialize the data"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialize the data changed"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


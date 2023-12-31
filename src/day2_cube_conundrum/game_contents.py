from src.utilities.split_strip import split_strip


class GameContents:
    def __init__(self, game_data):
        self.id = 0
        self.highest_red_count = 0
        self.highest_green_count = 0
        self.highest_blue_count = 0
        self.parse(game_data)

    def parse(self, game_data):
        id_text, games_text = game_data.split(":")
        self.id = int(id_text.split(" ")[1].strip())

        for game_text in games_text.split(";"):
            cubes = split_strip(game_text, ",")
            for cube in cubes:
                count_text, color, = split_strip(cube, " ")
                count = int(count_text)
                if color == "red":
                    if self.highest_red_count < count:
                        self.highest_red_count = count
                elif color == "green":
                    if self.highest_green_count < count:
                        self.highest_green_count = count
                elif color == "blue":
                    if self.highest_blue_count < count:
                        self.highest_blue_count = count

def analyze(self):

        # Procedural test of the colors values (Work in progress)
        message = 'Hello, my name is #' + str(self.hex) + ' and I am a '

        # Saturation test
        if (self.saturation >= 0.0 and self.saturation <= 0.3):
            message += 'desaturated '
        if (self.saturation >= 0.3 and self.saturation <= 0.6):
            message += 'saturated '
        if (self.saturation >= 0.6 and self.saturation <= 1.0):
            message += 'very saturated '

        # Lightness test
        if (self.lightness >= 0.0 and self.lightness <= 0.3):
            message += 'dark '
        if (self.lightness >= 0.3 and self.lightness <= 0.6):
            message += 'light '
        if (self.lightness >= 0.6 and self.lightness <= 1.0):
            message += 'brighter '

        # Tonal test
        # Color wheel - Each 1 / 12  = (0.08333333333333333)
        increment = (1.0 / 12.0)

        # - Red         is between 0 * increment and 1 * increment
        if (self.hue >= 0 * increment and self.hue <= 1 * increment):
            message += 'red color '
        # - Crimson     is between 1 * increment and 2 * increment
        if (self.hue >= 1 * increment and self.hue <= 2 * increment):
            message += 'crimson color '
        # - Magenta     is between 2 * increment and 3 * increment
        if (self.hue >= 2 * increment and self.hue <= 3 * increment):
            message += 'magenta color '
        # - Violet      is between 3 * increment and 4 * increment
        if (self.hue >= 3 * increment and self.hue <= 4 * increment):
            message += 'violet color '
        # - Blue        is between 4 * increment and 5 * increment
        if (self.hue >= 4 * increment and self.hue <= 5 * increment):
            message += 'blue color '
        # - Cobalt      is between 5 * increment and 6 * increment
        if (self.hue >= 5 * increment and self.hue <= 6 * increment):
            message += 'cobalt color '
        # - Cyan        is between 6 * increment and 7 * increment
        if (self.hue >= 6 * increment and self.hue <= 7 * increment):
            message += 'cyan color '
        # - Turqoise    is between 7 * increment and 8 * increment
        if (self.hue >= 7 * increment and self.hue <= 8 * increment):
            message += 'turquoise color '
        # - Green       is between 8 * increment and 9 * increment
        if (self.hue >= 8 * increment and self.hue <= 9 * increment):
            message += 'green color '
        # - Lime        is between 9 * increment and 10 * increment
        if (self.hue >= 9 * increment and self.hue <= 10 * increment):
            message += 'lime color '
        # - Yellow      is between 10 * increment and 11 * increment
        if (self.hue >= 10 * increment and self.hue <= 11 * increment):
            message += 'yellow color '
        # - Orange      is between 11 * increment and 12 * increment
        if (self.hue >= 11 * increment and self.hue <= 12 * increment):
            message += 'orange color '

        return message

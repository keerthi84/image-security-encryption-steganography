from PIL import Image


class IMG:
    """
    Simple LSB image steganography helper.

    Compatible with:
        s = steg_img.IMG(payload_path='secret.png', image_path='cover.png')
        s.hide()

        s = steg_img.IMG(image_path='stego.png')
        s.extract()
    """

    def __init__(self, image_path, payload_path=None):
        self.image_path = image_path
        self.payload_path = payload_path

    def hide(self, output_path=None):
        if self.payload_path is None:
            raise ValueError("Payload image path is required for hiding.")

        output_path = output_path or "stego.png"

        cover = Image.open(self.image_path).convert("RGB")
        payload = Image.open(self.payload_path).convert("RGB")

        # Store original payload size in first two pixels:
        # width high/low bytes, height high/low bytes.
        payload_width, payload_height = payload.size

        if payload_width > 65535 or payload_height > 65535:
            raise ValueError("Payload image is too large.")

        # Resize payload to cover size for a simple visible extraction demo.
        payload = payload.resize(cover.size)

        cover_pixels = cover.load()
        payload_pixels = payload.load()

        # Embed metadata in first two pixels
        cover_pixels[0, 0] = (
            (cover_pixels[0, 0][0] & 0xFE) | ((payload_width >> 15) & 1),
            (cover_pixels[0, 0][1] & 0xFE) | ((payload_width >> 14) & 1),
            (cover_pixels[0, 0][2] & 0xFE) | ((payload_width >> 13) & 1),
        )

        for x in range(cover.width):
            for y in range(cover.height):
                r, g, b = cover_pixels[x, y]
                pr, pg, pb = payload_pixels[x, y]

                # Hide the most significant bit of each payload channel
                # inside the least significant bit of each cover channel.
                r = (r & 0xFE) | ((pr >> 7) & 1)
                g = (g & 0xFE) | ((pg >> 7) & 1)
                b = (b & 0xFE) | ((pb >> 7) & 1)

                cover_pixels[x, y] = (r, g, b)

        cover.save(output_path)
        print("Stego image created:", output_path)

    def extract(self, output_path=None):
        output_path = output_path or "extracted.png"

        stego = Image.open(self.image_path).convert("RGB")
        extracted = Image.new("RGB", stego.size)

        stego_pixels = stego.load()
        extracted_pixels = extracted.load()

        for x in range(stego.width):
            for y in range(stego.height):
                r, g, b = stego_pixels[x, y]

                # Extract hidden LSBs and scale them for visibility.
                er = (r & 1) * 255
                eg = (g & 1) * 255
                eb = (b & 1) * 255

                extracted_pixels[x, y] = (er, eg, eb)

        extracted.save(output_path)
        print("Extracted image created:", output_path)

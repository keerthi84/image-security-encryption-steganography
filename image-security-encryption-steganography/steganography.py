import argparse
from steg import steg_img


def arguments():
    parser = argparse.ArgumentParser(
        description="Image Steganography Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-c", dest="carrier", type=str, default=None,
                        help="Path to the carrier image file.")

    parser.add_argument("-p", dest="payload", type=str, default=None,
                        help="Path to the payload image file. If omitted, extraction is performed.")

    parser.add_argument("-o", dest="output", type=str, default=None,
                        help="Output file path.")

    args = parser.parse_args()

    if args.carrier is None:
        print("[!] No carrier supplied.")
        parser.print_help()
        exit(0)

    return args


if __name__ == "__main__":
    args = arguments()
    carrier = args.carrier
    payload = args.payload
    output = args.output

    try:
        if payload is None:
            s = steg_img.IMG(image_path=carrier)
            s.extract(output_path=output)
        else:
            s = steg_img.IMG(payload_path=payload, image_path=carrier)
            s.hide(output_path=output)

    except Exception as err:
        print(err)

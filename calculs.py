import argparse
import re


def format_keys_per_second(kps):
    if kps < 1e3:
        return f"{kps:.2f}"
    elif kps < 1e6:
        return f"{kps / 1e3:.2f}K"
    elif kps < 1e9:
        return f"{kps / 1e6:.2f}M"
    else:
        return f"{kps / 1e9:.2f}B"


def valid_hex_range(option):
    match = re.fullmatch(r'([0-9a-fA-F]+):([0-9a-fA-F]+)', option)
    if match:
        return match.groups()
    raise argparse.ArgumentTypeError(f'Invalid hex range: {option}')

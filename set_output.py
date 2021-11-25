import argparse
import os


def main() -> int:
    for k, v in sorted(os.environ.items()):
        if 'INPUT' in k:
            print(f'{k}: {v}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

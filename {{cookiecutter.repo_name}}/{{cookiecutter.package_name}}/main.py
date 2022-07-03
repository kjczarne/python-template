import argparse


def main():
    parser = argparse.ArgumentParser(prog='{{cookiecutter.package_name}}', description='{{cookiecutter.package_description}}')
    parser.add_argument('-i', '--input', help='input', type=str)
    parser.add_argument('-o', '--output', help='output', type=str)

    args = parser.parse_args()

    print(f"INPUT: {args.input}")
    print(f"OUTPUT: {args.output}")


if __name__ == "__main__":
    main()


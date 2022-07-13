import sys
import cv2


def main() -> None:
    input_path = sys.argv[1]
    src_img = cv2.imread(input_path)
    if src_img is None:
        raise Exception()

    cvt_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", cvt_img)


if __name__ == "__main__":
    main()

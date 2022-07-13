import sys
import cv2


def main() -> None:
    input_path = sys.argv[1]
    src_img = cv2.imread(input_path)
    if src_img is None:
        raise Exception()

    cvt_code_dict = {
        cv2.COLOR_BGR2GRAY: "GRAY",
        cv2.COLOR_BGR2BGRA: "BGRA",
        cv2.COLOR_BGR2HSV: "HSV",
        cv2.COLOR_BGR2Lab: "Lab",
        cv2.COLOR_BGR2Luv: "Luv",
        cv2.COLOR_BGR2HLS: "HLS",
        cv2.COLOR_BGR2YUV: "YUV",
        cv2.COLOR_BGR2XYZ: "XYZ",
        cv2.COLOR_BGR2YCrCb: "YCrCb",
    }

    for code, v in cvt_code_dict.items():
        cvt_img = cv2.cvtColor(src_img, code)
        if len(cvt_img.shape) == 2:
            split_img = [cvt_img]
        else:
            split_img = [cvt_img[:, :, i] for i in range(len(cvt_img.shape))]

        for i in range(len(split_img)):
            cv2.imwrite(v + "_" + str(i) + ".png", split_img[i])


if __name__ == "__main__":
    main()

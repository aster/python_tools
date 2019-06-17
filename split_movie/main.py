import mov2frame as m2f

# 動画のパス
path = "./mov/MVI_3757.MOV"
# フレーム分割した画像を保存するディレクトリ
save_dir = "./image/"


def main():
    m2f.video_2_frames(path, save_dir)


if __name__ == "__main__":
    main()

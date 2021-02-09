# generate building images

reference:  
https://spjai.com/pix2pix-image-generation/

# setup enviroment
1. dockerをビルドする  
`docker-compose build`
2. dockerコンテナを立ち上げる  
`docker-compose up`  
デーモンで立ち上げる場合は`-d`をつける
3. コンテナ内に入る
`docker-compose exec python bash`
## create dataset
1. `images/original`に画像データを入れる
2. 必要ならファイル名を変更する `python rename_file.py`
3. ファイルサイズを統一する(256) `python resize.py`
4. 輪郭データを取得（ラベルとして使用する） `python get_contour.py`
5. 学習データとテストデータに分ける `python split_data.py`

## generate images

## train

### start train from trained model
`results/npz/snapshot_iter_hogehoge.npz`を利用して、途中から学習を始めることができる  
command ``
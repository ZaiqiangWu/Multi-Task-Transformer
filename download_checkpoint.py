import gdown

id = "1r0ugzCd45YiuBrbYTb94XVIRj6VUsBAS"
output = './InvPT_pascal_vitLp16.pth.tar'
gdown.download(f"https://drive.google.com/uc?export=download&confirm=pbef&id="+id,output)
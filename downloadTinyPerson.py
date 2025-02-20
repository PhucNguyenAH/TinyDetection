import openxlab
from openxlab.dataset import info, get, download

openxlab.login(ak="6mvd5yv36692bwdebnrg", sk="vd4woee015vyzwrnomll4wwx0dqpxlnypzggjqa7", relogin=True)
# print(info(dataset_repo='OpenDataLab/TinyPerson'))
# get(dataset_repo='OpenDataLab/TinyPerson', target_path='./data/')
# download(dataset_repo='OpenDataLab/TinyPerson',source_path='/raw/annotations.tar', target_path='./data/tinyperson/')
# download(dataset_repo='OpenDataLab/TinyPerson',source_path='/raw/test.tar.gz', target_path='./data/tinyperson/')
download(dataset_repo='OpenDataLab/TinyPerson',source_path='/raw/train.tar.gz', target_path='./data/tinyperson/')

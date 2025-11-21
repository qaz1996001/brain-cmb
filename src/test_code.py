import pathlib
from brain_cmb.dicomseg.builder import main_review_cmd

if __name__ == '__main__':
    # /mnt/e/pipeline/sean/rename_nifti/07263648_20190319_MR_20803190073
    _id       = '07263648_20190319_MR_20803190073'
    path_dcms = pathlib.Path('/mnt/e/pipeline/sean/rename_dicom/07263648_20190319_MR_20803190073/SWAN')
    path_nii  = pathlib.Path('/mnt/e/pipeline/sean/rename_nifti/07263648_20190319_MR_20803190073/Pred_CMB.nii.gz')
    path_dcmseg = pathlib.Path('/mnt/e/pipeline/sean/rename_nifti')
    print('main_review_cmd',)
    main_review_cmd(_id, path_dcms, path_nii, path_dcmseg)
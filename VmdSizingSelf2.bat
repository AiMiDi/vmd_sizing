@echo off
rem --- 
rem ---  vmd�f�[�^�̃g���[�X���f����ϊ�
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

rem ---  ����vmd�t�@�C���p�X


rem set INPUT_VMD=vmd\�J�g�����[���[�V����(�R�������~�NV3_Re).vmd
rem set INPUT_VMD=vmd\�h�[�i�c�z�[��.vmd
rem set INPUT_VMD=vmd\egorock_miku.vmd
rem set INPUT_VMD="vmd\VIVA Funny Day.vmd"
rem set INPUT_VMD=vmd\animaru-1.vmd
rem set INPUT_VMD=vmd\�x�m�����[�V����.vmd
rem set INPUT_VMD=vmd\�����J����.vmd
rem set INPUT_VMD=vmd\������������.vmd
rem set INPUT_VMD="vmd\�_���X���[�V�����i�����{�[��_�߂�ڂ��������~�N�j.vmd"
rem set INPUT_VMD="vmd\���Ɍ����Ă���B�_���X_���T.vmd"
rem set INPUT_VMD="vmd\�_���X���[�V�����i������_�炢�����s�A�X�̏��N�j.vmd"
rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\ONE_OFF_MIND yurie\ONE_OFF_MIND.vmd"

rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\���Ⴟ�� �w�^���A�C�M���Xv1.032\�w�^���A�C�M���Xv1.032.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\ISAO���~�N\I_�~�Nv4\Miku_V4_���W��.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\128_���c�ѐ���\���c�ѐ������炫�� ver.1.04\���c�ѐ^���K�E.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ�����]ver1.2 azure��\�ɂ�����](����)ver1.2_160.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ�����]ver1.2 azure��\�ɂ�����]ver1.2.pmx"



rem set INPUT_VMD=vmd\lamb���{�[�������l�p.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�퍑BASARA\�K�� ���ʂ��� ver.1.24\�^�c�K���v���ߑ�1.24.pmx"

rem set INPUT_VMD="vmd\VIVA Funny Day(��0.9).vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\�J�����������~�Nver2.0\�J�����������~�N.pmx"

rem set INPUT_VMD="vmd\2.����10L_(40f_�O�ړ�20)_�S�Ă̐e.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\�J�����������~�Nver2.0\�J�����������~�N.pmx"

rem set INPUT_VMD="vmd\100-end_�j��A-����-���i���ҋ@(�v�㔼�g2).vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\���C�E���B���@���f�B Ver GA1.0 CPUX4\Ray\Ray.pmx"

rem set INPUT_VMD="vmd\�j�x��_���i.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\roco�����{_ver1.00b\roco�����{_ver1.00b_�l�p.pmx"

rem set INPUT_VMD="vmd\���˂����_�[����_Tda��.vmd"
rem set INPUT_VMD="vmd\���˂����_�[����_Tda��_200f.vmd"
rem set INPUT_VMD="vmd\���˂����_�[����_Tda��_�n�[�g.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="vmd\���W���~�N�荇�킹.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�h���}�c���M�[ motion �z�z�p moka\�h���}�c���M�[.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_2�l\�A���r���[�o�[�Y_���[�V���� �˂��낤\�A���r���[�o�[�Y_�_���X���[�V����(�����ʒu_�E).vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\003_�O�����@��\�O�����@�� �킿�� �i���~���C���i�[���j\�킿���O�����@�߁i���~���C���i�[���j.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_2�l\�A���r���[�o�[�Y_���[�V���� �˂��낤\�A���r���[�o�[�Y_�_���X���[�V����(�����ʒu_��).vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\005_���ϊ�\���ϊ� mono\���ϊ�.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�^��\�ǏR��o�N�]���[�V���� �O���C\�ǏR��o�N�].vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_3�l\���C�A�[�_���X�z�z�p���[�V���� moka\���ʖڐ�\miku.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="vmd\�A�f�B�V���i���������[���[�V����.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ�����]ver1.2 azure��\�ɂ�����]ver1.2.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�͂��炫�����Ȃ��ł����郂�[�V���� ��ؗ�\�͂��炫�����Ȃ��ł����郂�[�V����0906.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�_�Ђ�����\YM���_�Ђ�����v13\�_�Ђ�����v1_3.pmx"

rem set INPUT_VMD=vmd\musicx2.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\�߂�ڂ��� �����~�N Ver1.11\�߂�ڂ��� �����~�N ver1.11.pmx"

rem set INPUT_VMD=vmd\��]�e�X�g.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="vmd\�n���Ō�̍�����v106_���҃~�N_�r����L.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"

rem set INPUT_VMD=vmd\�n���Ō�̍�����v106_���҃~�N_962-1000.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�J�K���r�g �������[\�J�K���r�g.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\kurokuma���X�E�F�[�f���R��2��ver.2.71\�w�^���A�E�X�E�F�[�f��Ver.2.71\�X�E�F�[�f��ver.2.71.pmx"

rem set INPUT_VMD=C:\MMD\vmd_sizing\vmd\test_Tda.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"


rem set INPUT_VMD="vmd\������Ⴀ���S\������Ⴀ�j��.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\���l��\�l�C�L�b�h�E�X�l�[�Nver0.60 ��܂΂�\�l�C�L�b�h�E�X�l�[�N ver0.60.pmx"

rem set INPUT_VMD="vmd\��onmyway.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\Fate\�����ς񎮉��c�ȑ� Ver1.2\04_�X�[�c\���c�ȑ��i�V���c�j.pmx"


rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\���Z�m���[�V���� mika\���Z�m���[�V����.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�i���̋��l\�G�����B��ver.2.4-a1dou3\�G�����B��-2.4[�V���c].pmx"


rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�A���m�E���E�}�U�[�O�[�X �Q�b�c�^kemo\Unknown_���ɂ܂����~�NALL.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD=vmd\���˂����_�[����_Lat��_0-200f.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Lat���~�NVer2.31\Lat���~�NVer2.31_Normal_���W��.pmx"


rem set INPUT_VMD=vmd\���˂����_�[����_Tda��_200f.vmd
rem set INPUT_VMD="vmd\���˂����_�[����_Tda��.vmd"
rem set INPUT_VMD="vmd\���˂����_�[����_Tda��_886-965.vmd"
rem set INPUT_VMD="vmd\���˂����_�[����_Tda��_�n�[�g.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="vmd\�A���m�E���}�U�[�O�[�X�y�t�B���K�[�^�b�g���[�V�����z1.00.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\112_�G��\�G��mkmk009b ��������\�G��mkmk009b\�G�ۓ���mkmk009b.pmx"

rem set INPUT_VMD=vmd/�Y�B�߃��[�V����.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�d���e�g\Tda���d���e�g�`���C�i\tda���d���e�g�`���C�iver2.pmx"

rem set INPUT_VMD=vmd/�Y�B�߃��[�V����_0-880_2.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�d���e�g\Tda���d���e�g�`���C�i\tda���d���e�g�`���C�iver2.pmx"

rem set INPUT_VMD=vmd\shakeit_rin_0-100.vmd
rem set INPUT_VMD=vmd\shakeit_rin_556-691.vmd
rem set INPUT_VMD=vmd\shakeit_rin.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\��������\��������AppendXS mqdl\rinApXS.pmx"

rem set INPUT_VMD=vmd\�����p��.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD=vmd\�r�Ȃ�_���肢.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"

rem set INPUT_VMD=vmd\�D�n�V�K���[�V����ver1.01.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\025_�����U\�����U �Ђ킱�� ver.2.0\�����U(�Ђ킱��) ver.2.0.pmx"

rem set INPUT_VMD=vmd\egorock_miku.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\ISAO���~�N\I_�~�Nv4\Miku_V4_���W��.pmx"

rem set INPUT_VMD=vmd\�E�؎荇�킹.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"

rem set INPUT_VMD=vmd\��������_�m�[�}��Tda���p.vmd
rem set INPUT_VMD=vmd\��������_0-500f.vmd
rem set INPUT_VMD=vmd\��������_2164-2227.vmd
rem set INPUT_VMD=vmd\��������_2036-2353f.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�^��\����(�����u��) �O���C\���[�V��������20190625.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"

rem set INPUT_VMD=vmd\�ɂ񂶂��΂�΂�Miku�i�C���Łj.vmd
rem set INPUT_VMD=vmd\�ɂ񂶂��΂�΂�`��.vmd
rem set INPUT_VMD=vmd\�ɂ񂶂��΂�΂�0-800f.vmd
rem set INPUT_VMD=vmd\�ɂ񂶂��΂�΂�3166-3213f.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD="vmd\Love Me If You Can.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\025_�����U\�����U �Ђ킱�� ver.2.0\�����U(�Ђ킱��) ver.2.0.pmx"

rem set INPUT_VMD=vmd\�x�m�����[�V����.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"


rem set INPUT_VMD=vmd\nekomimi_mikuv2.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD=vmd\�N���u�}�W�F�X�e�B.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�퍑BASARA\�K�� ���ʂ��� ver.1.24\�^�c�K���v���ߑ�1.24.pmx"

rem set INPUT_VMD=vmd\�ǂ��������ƂȂ�_���[�V����.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\�H�ǎ����}�[�mver.2.1\���}�[�mver.2.1.pmx"

rem set INPUT_VMD=vmd\���o�[�V�u���E�L�����y�[��_���Ƃ������(�g���X�����f��).vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"

rem set INPUT_VMD=vmd\�A���r�o�����c�z�z�p(�E��008c).vmd
rem set INPUT_VMD=vmd\�A���r�o�����c�z�z�p(�E��008c)_3260-3933f.vmd
rem set INPUT_VMD=vmd\�A���r�o�����c�z�z�p(�E��008c)_6115-6369f.vmd
rem set INPUT_VMD=vmd\�A���r�o�����c�z�z�p(�E��008c)_6597-6728.vmd
rem set INPUT_VMD=vmd\�A���r�o�����c�z�z�p(�E��008c)_0000-0300f.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"


rem set INPUT_VMD=vmd\�r�L�[�Ȃ�.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\���C�A�[�_���Xteto_2930-3100f.vmd
rem set INPUT_VMD=C:\MMD\vmd_sizing\vmd\���C�A�[�_���Xteto_4767-4906f.vmd
rem set INPUT_VMD=vmd\���C�A�[�_���Xteto.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�d���e�g\Tda�����σe�g�E���񂶂���ccv�Z�b�gVer1.01 coa\Tda�����σe�g�E���񂶂���ccv ver.1.01\Tda�����σe�g�E���񂶂���ccv Ver1.01.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�d���e�g\Tda���d���e�gTypeS\Tda���d���e�gTypeS.pmx"

rem set INPUT_VMD=vmd\�]�p�o�����[�R.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ�����]ver1.0 �X�q����\�X�q�����ɂ�����]_�e�w0�ǉ�.pmx"

rem set INPUT_VMD=vmd\�~�N�p�o�����[�R.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD=vmd\���j�o�[�X�R������.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\�R������  �����~�NV3_Re_rev.1.2\�R������  �����~�NV3_Re_rev.1.2(�X�p�b�c)_���W��.pmx"

rem set INPUT_VMD=vmd\kinoko_right.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\��Ԏ����у~�N�E�l�� White �i����������ϔŁj\��Ԏ����у~�N_White\��Ԏ����у~�N_Wv3_���W��.pmx"

rem set INPUT_VMD=vmd\����X�J�[�g.vmd
rem set INPUT_VMD=vmd\����X�J�[�g_0000-0501.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\���N�ŗ�K�[��_Tda��-���s�p�[�g.vmd
rem set INPUT_VMD=vmd\���N�ŗ�K�[��_Tda��-�����Ă��񂱃p�[�g.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\�ɂ񂶂��΂�΂�_�q�J��.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\GUMI\�܂܂܎�GUMI ��\GUMI���ŏC�����W��.pmx"

rem set INPUT_VMD=vmd\�f�t�H���g���.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��2B�Ή�_20190708_���Ȃ�.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�NV4X_Ver1.00\Tda�������~�NV4X_Ver1.00.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_2�l\�҂����M�ы����[�V���� bataki\�҂����M�ы�������.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�^��\MikuMikuDance�Ń��W�I�̑����(�~�N��ver) current\radio1_miku.vmd"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"

rem set INPUT_VMD=vmd\���o�[�V�u���E�L�����y�[��_���Ƃ������(�g���X�����f��).vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"

rem set INPUT_VMD=vmd\�Ő�~_���Ƃ������.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"

rem set INPUT_VMD=vmd\�A���O��.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\Vtuber\�~���C �A�J��_v1.0\MiraiAkari_v1.0.pmx"

rem set INPUT_VMD=vmd\loki_miku_konafuki2.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\ISAO���~�N\I_�~�Nv4\Miku_V4_���W��.pmx"

rem set INPUT_VMD=vmd\�_���V���O�E�q�[���[_�Z���^�[.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\���에��.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\�ʂ��񃂁[�V����20190716.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\�x��}�l�L��Ver.2 ��������\�x�钆���}�l�L��_��.pmx"

rem set INPUT_VMD=vmd\�ʂ��񃂁[�V����20190717_4.vmd
rem set INPUT_VMD=vmd\�ʂ��񃂁[�V����20190717_4_�����Z.vmd
rem set INPUT_VMD=vmd\�ʂ��񃂁[�V����20190717_4_�����l����.vmd
rem set INPUT_VMD=vmd\�ʂ��񃂁[�V����20190717_4_2.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

rem set INPUT_VMD=vmd\�h���}�c���M�[_moka_S��.vmd
rem set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"

set INPUT_VMD=vmd\�ߊۃe�X�g20190731.vmd
set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx"
















rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\091_�a��猓��\�a��猓�� �킩�� ver.2.0\�킩���a��猓��(����)ver.2.0.pmx"
rem set REPLACE_MODEL_PMX=D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\Tda�������~�N�E�A�y���hVer1.00\Tda�������~�N�E�A�y���h_Ver1.00.pmx
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\ISAO���~�N\I_�~�Nv4�`���C�i\Miku_V4_���`���C�i.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\roco���t�����X_ver1.02\roco���t�����X_CD_ver1.02.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\mkmk���@�w�^���A�E�h�C�c�imkmk)014(046)��\�h�C�c�imkmk)014(046)��\�h�C�c�R�� mkmk 031�@�w�^���A\�h�C�c�R��   mkmk031�@�w�^���A.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\061_�������r\�������r �ۂ񂸎� ver1.00\�ۂ񂸎��������rver1.00.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\059_�u��\�u�� roco�� ver1.03\roco���u��_ver1.03_���Ȃ�.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\045_�����l�Y\�����l�Y  �����㎮ ��\�����l�Y.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\045_�����l�Y\�����l�Y �����㎮ ��\�ɗ�.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\039_�O�c���l�Y\�O�c���l�Y �|�G���� v1.35\�O�c���l�Y_�ʏ�.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\035_�㓡���l�Y\�㓡���l�Y ���^�J�� ver1.3\�ʏ풆�����Ԑ^��\�㓡���l�Y1.3(155).pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\047_�܌Ց�\�܌Ց� ����� v1.42\�܌Ց�.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\009_��Z\��Z mkmk�� ���~�� 002\��Z�y���~���zmkmk002\��Z�y���~��3�zmkmk002 ��������.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90_T�X�^���X.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\055_���\��� ���Ƃ��� ver0.90\���Ƃ������ver0.90_�Ђ��Ȃ���.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\027_�Δ����l�Y\�Δ����l�Y ���₿�厮 ver1.12\���₿�厮�Δ����l�Yver1.12.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\041_�H�c���l�Y\�H�c���l�Y �������� v1.0\���������H�c���l�Yv1.0.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\041_�H�c���l�Y\�H�c���l�Y �|�G���� v1.6\�H�c���l�Y.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�h���N�G\���_���O���C�O�z�z�pver1.09��2\���_���O���C�O.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�h���N�G\�yMMD�z�}���e�B�iVer.0.58\���}���e�B�iver.0.58.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�h���N�G\�h����d����\�}�W�F�Z�h����.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\Fate\��捂̃n�T�� �݂���\��捂̃n�T��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\059_�u��\�u�� ���� mqdl\�u��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\043_�������l�Y\�������l�Y �������� v1.32\�������l�Yv1.32.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\013_��T������\�ʏ����_ver0.24 �`\oden_0_24.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�A���W�F���[�N\�I�X�J�[(Ver.1.2) �����鎮\�����鎮�I�X�J�[.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ�����]ver1.2 azure��\�ɂ�����]ver1.2.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�A�C�}����\�A�C�}��������� Vol.03 ver1.0\�A�C�}���������Vol.03_���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�A�C�}����\�A�C�}��������� Vol.03 ver1.0\�A�C�}���������Vol.03_���W��_A�X�^���X.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�W���W��\�W���i�T��ver1.1\�W���i�T���E�W���[�X�^�[_���{�[��.pmx"


rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\mkmk���@AP�w�^���A�E�n���K���[mkmk�S��017B\�n���K���[mkmk�S��017B\�n���K���[�@�G�v�����h���X�@016\�n���K���[�@�G�v�����h���X��mkmk017.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\QM���w�^���A�E�n���K���[ver.1.02\QM���n���K���[ver.1.02.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\045_�����l�Y\�����l�Y ���F�� ��\�����l�Y(�ʏ�).pmx"

set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�q�v�}�C\�ٓ����q�v�}�C�f�t�H����12ver.1.01\�ٓ����f�t�H������������\�ٓ����f�t�H������������ver.1.00.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�d���e�g\Tda���d���e�g�`���C�i\tda���d���e�g�`���C�iver2.pmx"


rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\118_�ւ��ؒ��J��\�͂��� ���Γ��� 0.22\���Γ����͂���0.22.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\019_�ɂ�����]\�ɂ����肠���� nano ��\nano�ɂ�����]-����.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�y�����z����mkmk002b\�E�؁y�����zmkmk002a�����j�m\�E�ؓ����j�mmkmk002a.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�y�����z����mkmk002b\�G�ہy�����zmkmk002�����j�m\�G�ۓ����j�mmkmk002.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\128_���c�ѐ���\���c�ѐ������炫�� ver.1.04\���c�ѐ^���K�E.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\095_�R�W�؍��L\�˂񕗎R�W�؃Y_v05 Zinia\158\�˂񕗎R�W�ؒ��`���ԁi��j.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\095_�R�W�؍��L\�˂񕗎R�W�؃Y_v05 Zinia\96\�˂񕗎R�W�؍��L�Ɂi��j.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\095_�R�W�؍��L\�˂񕗎R�W�؃Y_v05 Zinia\158\�˂񕗎R�W�ؒ��`���ԁi��j.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\095_�R�W�؍��L\�˂񕗎R�W�؃Y_v05 Zinia\158\�˂񕗎R�W�ؒ��`���ԁi���j.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�y�����z����mkmk002b\�E�؁y�����zmkmk002a�����j�m\�E�ؓ����j�m��mkmk002a.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�y�����z����mkmk002b\�E�؁y�����zmkmk002a�����j�m\�E�ؓ����j�mmkmk002a.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\152_�Ì`�㓁\�Ì`�㓁�݂�����[��0.52\�Ì`�㓁���뎮0.52.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\140_�b�`�㓁\�b�`�㓁 �݂�����[�� Ver.0.87\�b�`�㓁�݂�����[��0.87.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\�{���~�A �r���{\�{���~�A���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�h���S���{�[��\�����ver3,02 ���낽\��󓹒�\��󓹒�160530.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\���{�b�g\�^�C���}�W�[�� �i�G�e�B�}�X\�^�C���}�W�[��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\meme�� �w�^���A_�I�[�X�g���A_ver1.03\�I�[�X�g���A�i5���\���jver 1.03.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\013_��T������\��T������ Msk�� ver1.0\Msk����T������_ver1.0.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\������\�j���g���Z�b�g Herring\���j���g��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\���Ⴟ�� �w�^���A�C�M���Xv1.032\�w�^���A�C�M���Xv1.032.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04_���p�J�i.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04_���p19����.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\���{�b�g\��Ζ��G�Z�b�gver1.53 ����\�n���h�q�g\�S�b�h���C�W���I�[.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�J�C�g���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������_���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\Fate\hoge��������ver1.00\hoge��������ver1.00.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�͑����ꂭ�����\��ǂ���r���^_rev20170829 less\�e��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�͑����ꂭ�����\��ǂ���r���^_rev20170829 less\�H��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\2B�i�����n��B�^�j Ver04.07 taka96\na_2b_0407.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\eve_v100_pmx\eve_���W��.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\������\�x��Lver1.02 �g���[�`\�D���˂�.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������.pmd"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�����~�NVer2 ���W��2B�Ή�_20190708.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b.pmx"
rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E��mkmk(Se)009b_�Ђ��Ȃ���.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\011_����\���� ���� ver0124\���C�u�ߑ�\�����C���i�[.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\007_�ΐ؊�\�ΐ؊� �X�q���� ver1.4�i�݂قƂ��ߑ��j\�X�q�����ΐ؊ہi�݂قƂ���O�j.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�������\�������_�ėэˎq_�����׎��z�z�p_ver0.5.3\�������_�ėэˎq.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�͑����ꂭ�����\prinzeugen �(�����ۂ�)\prinzeugen.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�w�^���A\�H�ǎ����}�[�mver.2.1\���}�[�mver.2.1.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\���҃~�N01_Ver.1.04 �A�����E�x����\Appearance Miku_01_Ver.1.04.pmx"

rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\089_�̐匓��\�˂� ��̂��� �̐匓��1.01\��̂����˂񕗉̐匓��1.01.pmx"

rem set REPLACE_MODEL_PMX=%MODEL_PMX%




rem set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\�I���W�i��\�x��}�l�L��Ver.2 ��������\�x�钆���}�l�L��_��.pmx"

set INPUT_VMD="D:\MMD\MikuMikuDance_v926x64\UserFile\Motion\�_���X_1�l\�����tIII �Ȃ�\nac_aikotoba3_pick.vmd"
set MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\��Ԏ��~�N\��Ԏ��~�N_���W��.pmx"
rem set REPLACE_MODEL_PMX=D:\MMD\MikuMikuDance_v926x64\UserFile\Model\��������\107_�E��\�E��mkmk009c ��������\�E��mkmk009c\�E�؏㒅��mkmk009b.pmx
set REPLACE_MODEL_PMX="D:\MMD\MikuMikuDance_v926x64\UserFile\Model\VOCALOID\�����~�N\��Ԏ��~�N\��Ԏ��~�N_���W��.pmx"


SETLOCAL enabledelayedexpansion
rem set TEST_PARAM_X=1,0,1-,1.75,1.75-
rem set TEST_PARAM_Y=1.75,1.75-,1,0,1-
rem set TEST_PARAM_Z=0,1-,1.75,1.75-,1
set TEST_PARAM_X=1,0,1-
set TEST_PARAM_Y=1-,1,0
set TEST_PARAM_Z=0,1-,1

for %%x in (%TEST_PARAM_X%) do (
    for %%y in (%TEST_PARAM_Y%) do (
        for %%z in (%TEST_PARAM_Z%) do (
            
            set NOW_TEST_X=%%x
            set NOW_TEST_Y=%%y
            set NOW_TEST_Z=%%z
            echo NOW_TEST_X !NOW_TEST_X!
            echo NOW_TEST_Y !NOW_TEST_Y!
            echo NOW_TEST_Z !NOW_TEST_Z!
            
            set TEST_PARAM=!NOW_TEST_X!,!NOW_TEST_Y!,!NOW_TEST_Z!
            echo TEST_PARAM !TEST_PARAM!
            set OUTPUT_PATH="E:\MMD\vmd_sizing\vmd\input_slope23\slope30_!TEST_PARAM!.vmd"
                            
rem ---  python ���s
python src/main.py --vmd_path %INPUT_VMD%  --trace_pmx_path "%MODEL_PMX%"  --replace_pmx_path "%REPLACE_MODEL_PMX%"  --output_path "!OUTPUT_PATH!"  --test_param "!TEST_PARAM!"  --avoidance 0  --avoidance_finger 0  --hand_ik 0  --hand_distance 1.7  --floor_hand 0  --floor_hand_up 1  --floor_hand_down 1  --hand_floor_distance 1.8  --leg_floor_distance 1.5  --finger_ik 0  --finger_distance 1.4  --vmd_choice_values ""  --rep_choice_values ""  --rep_rate_values ""  --camera_vmd_path ""  --camera_pmx_path ""  --camera_y_offset 0  --verbose 2
        )
    )
)

rem set TEST_PARAM_X=x,x-,y,y-,z,z-
rem set TEST_PARAM_Y=y,y-,z,z-,x,x-
rem set TEST_PARAM_Z=z,z-,x,x-,y,y-
rem 
rem for %%x in (%TEST_PARAM_X%) do (
rem     for %%y in (%TEST_PARAM_Y%) do (
rem         for %%z in (%TEST_PARAM_Z%) do (
rem             
rem             set NOW_TEST_X=%%x
rem             set NOW_TEST_Y=%%y
rem             set NOW_TEST_Z=%%z
rem             echo NOW_TEST_X !NOW_TEST_X!
rem             echo NOW_TEST_Y !NOW_TEST_Y!
rem             echo NOW_TEST_Z !NOW_TEST_Z!
rem             
rem             if !NOW_TEST_X! neq !NOW_TEST_Y! (
rem                 if !NOW_TEST_Y! neq !NOW_TEST_Z! (
rem                     set TEST_PARAM=!NOW_TEST_X!,!NOW_TEST_Y!,!NOW_TEST_Z!
rem                     echo TEST_PARAM !TEST_PARAM!
rem                     set OUTPUT_PATH="E:\MMD\vmd_sizing\vmd\input_slope23\slope28_!TEST_PARAM!.vmd"
rem                     
rem rem ---  python ���s
rem python src/main.py --vmd_path %INPUT_VMD%  --trace_pmx_path "%MODEL_PMX%"  --replace_pmx_path "%REPLACE_MODEL_PMX%"  --output_path "!OUTPUT_PATH!"  --test_param "!TEST_PARAM!"  --avoidance 0  --avoidance_finger 0  --hand_ik 0  --hand_distance 1.7  --floor_hand 0  --floor_hand_up 1  --floor_hand_down 1  --hand_floor_distance 1.8  --leg_floor_distance 1.5  --finger_ik 0  --finger_distance 1.4  --vmd_choice_values ""  --rep_choice_values ""  --rep_rate_values ""  --camera_vmd_path ""  --camera_pmx_path ""  --camera_y_offset 0  --verbose 2
rem                 )
rem             )
rem         )
rem     )
rem )





# �h���S�����[�X�ݒ� 2005/03/30 �R��

# -------- �ݒ蕔�� ---------

# ���[�X�ݒ�
@WEATHER=('��','�J');
@RACERANK=('G1','G2','G3','OP','100��','������');
@FIELDTYPE=('�Ő�','�_�[�g');

@RACETERM=("�o�����[�X","�d�܃��[�X");

@RACE=(
	# 0����		1�����N	2�n���f	3�n���	4�I�Ս�	5����	6�P��	7�Q��	8�R�� 9���
	[
	['��t�V��'	,5	,0	,0	,1	,1600	,50	,30	,20	,10],
	['�����Ԃ�񂩔t',4	,20	,0	,0	,1600	,100	,50	,30	,10],
	['�����Ԃ�񂩃_�[�g�t',4,20	,1	,1	,1600	,100	,50	,30	,10],
	['������2600�_�[�g',5	,0	,1	,0	,2600	,50	,30	,20	,10],
	['���������J�b�v',3	,50	,0	,0	,2800	,150	,70	,50	,10],
	['���������_�[�g�J�b�v',3,50	,1	,0	,2800	,150	,70	,50	,10],
	['�ʉԐV��'	,5	,0	,0	,0	,2200	,50	,30	,20	,10],
	['�����Ŕt'	,4	,20	,0	,0	,2000	,100	,50	,30	,10],
	['�����Ń_�[�g�t',4	,20	,1	,1	,2000	,100	,50	,30	,10],
	['������1600�_�[�g',5	,0	,1	,1	,1600	,50	,30	,20	,10],
	['����߃J�b�v',3	,50	,0	,1	,1400	,150	,70	,50	,10],
	['����߃_�[�g�J�b�v',3	,50	,1	,0	,1400	,150	,70	,50	,10],
	],
	[
	['����t�n���f'	,2	,100	,0	,0	,2600	,200	,100	,80	,10],
	['���ԏ�'	,2	,100	,1	,0	,2200	,200	,100	,80	,10],
	['�V���t'	,2	,100	,0	,0	,1600	,200	,100	,80	,10],
	['���V�t'	,2	,100	,0	,0	,2000	,200	,100	,80	,10],
	['�̎�`�������W�J�b�v',1,200	,0	,1	,2800	,300	,150	,100	,10],
	['���ԏ�'	,1	,200	,1	,0	,2200	,300	,150	,100	,10],
	['�����g���C�A���J�b�v',1,200	,0	,0	,1400	,300	,150	,100	,10],
	['���V�g���C�A���J�b�v',1,200	,0	,1	,2000	,300	,150	,100	,10],
	['�V��N������'	,0	,0	,0	,0	,3000	,400	,200	,100	,10],
	['�t�ԏ�'	,0	,0	,1	,1	,2400	,400	,200	,100	,10],
	['�H����'	,0	,0	,0	,1	,1600	,400	,200	,100	,10],
	['���̏�'	,0	,0	,0	,0	,2000	,400	,200	,100	,10],
	],
);

# �q��
$RCest=1000000;

# �����h���S��
$MYDRmax=3;
$DRbuy=500000;

# ����
$DRretire=86400 * 10;
$PRentry=300;
$PRcycle=86400 * 3;

# �X��
$STest=500000;
$STcost=100000;
$STmax=10;
$STtime=86400 * 50;

# �R��
$JKest=500000;
$JKmax=20;
$JKtime=86400 * 50;

# �R��\��
@JKSP=(
	'�Ȃ�',
	'�ė��̋R�悪����',
	'�����̋R�悪����',
	'�ł̃��[�X�ɋ���',
	'�_�[�g�̃��[�X�ɋ���',
	'�啑��ɋ���',
	'�J�̃��[�X�ɋ���',
	'��������Ɨ��̐����𑣂�',
);

# �p��̒�`

@STRATE=('����','��s','����','�Ǎ�','����');

@EMPHA=('�X�s�[�h','��������','�u����','�p���[','���N','�_�');

@VALUE=('�d','�c','�b','�a','�`','�r','�r');

@EVALUE=('�~','��','��','��','��');

@FM=('��','��');

@ONRACE=('�ҋ@','<b>���I</b>','<SPAN>�o�^</SPAN>','<SPAN>�o��</SPAN>');

@DRCOLOR=('�g��','��','�ɖ�','����','����');

# �X�V���� (�������� �o���o������ �d�܏o������)

@DRTIMESET=(3,23,22);

# -------- �ݒ芮�� ---------

@DLOG=();

@DRnamelist=qw(
		no birth fm color name town owner stable race apt
		sp spp sr srp ag agp pw pwp hl hlp fl flp
		con wt gr
		prize sdwin g3win g2win g1win
		);

@PRnamelist=qw(
		no birth fm color name town owner apt hr preg
		sp sr ag pw hl fl
		prize sdwin g3win g2win g1win
		);

@RCnamelist=qw(
		no birth name town owner
		prize sdwin g3win g2win g1win
		);

@STnamelist=qw(
		no birth name town owner
		emp tr con wt
		sp sr ag pw hl fl
		sdwin g3win g2win g1win
		);

@JKnamelist=qw(
		no birth name town owner race
		ahead back sp
		sdwin g3win g2win g1win
		);

@RDnamelist=qw(
		no dr birth fm color name ranch rcname stable stname jock jkname prize strate
		sp1 sp2 sp3 sp4
		pop time str lose
		);
1;

sub GetTagImgDra
{
	my($i,$ii,$old)=@_;
	$i++;
	$ii++;
	$i+=2 if $old;
	return qq|<IMG class="i" SRC="$IMAGE_URL/dragon$i$ii$IMAGE_EXT">|;
}


# �h���S�����[�X �R��ҏW 2005/03/30 �R��

ReadJock();
$disp.="<BIG>���h���S�����[�X�F�R��</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteJock();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYJK!=-1);
OutError("bad request") if (scalar @JK >= $JKmax);
OutError('�����̗]�T������܂���B') if ($DT->{money} < $JKest);

	# ���O�̐��������`�F�b�N
	require $JCODE_FILE;
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');

	if(!$Q{name})
	{
		OutError('���O����͂��Ă��������B');
	}
	if($Q{name} =~ /([,:;\t\r\n<>&])/ || CheckNGName($Q{name}) )
	{
		OutError('���O�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B');
	}
	OutError('���O���������܂��B') if length($Q{name})>20;
	OutError('���O���Z�����܂��B') if length($Q{name})<6;

	@JK=reverse(@JK);
	$JKcount++;
	my $i=$JKcount;
	$JK[$i]->{no}=($i > 0) ? ($JK[$i-1]->{no} + 1) : 1 ;
	$JK[$i]->{birth}=$NOW_TIME;
	$JK[$i]->{name}=$Q{name};
	$JK[$i]->{town}=$MYDIR;
	$JK[$i]->{owner}=$DT->{id};
	$JK[$i]->{ahead}=int(rand(15));
	$JK[$i]->{back}=int(rand(15));

	# �����t�^
	if ($JK[$i]->{ahead} > $JK[$i]->{back})
		{
		$JK[$i]->{ahead}+=15;
		}
		else
		{
		$JK[$i]->{back}+=15;
		}
	@JK=reverse(@JK);

WritePayLog($MYDIR,$DT->{id},-$JKest);
PushDraLog(0,"�V�����R��u".$Q{name}."�v���f�r���[���܂����B");
$disp.="�V�����R��u<b>".$Q{name}."</b>�v���ق��܂����B";
}


# �h���S�����[�X �X�ɕҏW 2005/03/30 �R��

ReadStable();
$disp.="<BIG>���h���S�����[�X�F�X��</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteStable();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYST!=-1);
OutError("bad request") if (scalar @ST >= $STmax);
OutError('�����̗]�T������܂���B') if ($DT->{money} < $STest);

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

	@ST=reverse(@ST);
	$STcount++;
	my $i=$STcount;
	$ST[$i]->{no}=($i > 0) ? ($ST[$i-1]->{no} + 1) : 1 ;
	$ST[$i]->{birth}=$NOW_TIME;
	$ST[$i]->{name}=$Q{name};
	$ST[$i]->{town}=$MYDIR;
	$ST[$i]->{owner}=$DT->{id};
	$ST[$i]->{emp}=$Q{emp};
	$ST[$i]->{sp}=1;
	$ST[$i]->{tr}=int(rand(15));
	$ST[$i]->{con}=int(rand(15));
	$ST[$i]->{wt}=int(rand(15));
	@ST=reverse(@ST);

WritePayLog($MYDIR,$DT->{id},-$STest);
PushDraLog(0,"�V�����X�Ɂu".$Q{name}."�v���ݗ�����܂����B");
$disp.="�V�����X�Ɂu<b>".$Q{name}."</b>�v��ݗ����܂����B";
}

sub large
{
OutError("bad request") if ($MYST==-1);
OutError('�����̗]�T������܂���B') if ($DT->{money} < $STest);
my $n=int(($NOW_TIME - $ST[$MYST]->{birth})/86400/2) + 1;
my $cost=($ST[$MYST]->{sp} + $ST[$MYST]->{sr} + $ST[$MYST]->{ag} + $ST[$MYST]->{pw} + $ST[$MYST]->{hl} + $ST[$MYST]->{fl});
OutError("bad request") if ($n < $cost);

	my @large=qw(
		sp sr ag pw hl fl
		);

	my $lar=$large[$Q{lar}];

	$ST[$MYST]->{$lar}++;
	OutError('����ȏ�C���̎{�݂͑��z�ł��܂���') if ($ST[$MYST]->{$lar} > 3);

WritePayLog($MYDIR,$DT->{id},-$STest);
$disp.="�X�ɂ𑝒z���܂����B";
}


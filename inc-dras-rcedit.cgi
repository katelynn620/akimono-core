# �h���S�����[�X �q��ҏW�\�� 2005/03/30 �R��

ReadRanch();
$disp.="<BIG>���h���S�����[�X�F�q��</BIG><br><br>";

my $functionname=$Q{code};
OutError("bad request") if !defined(&$functionname);
&$functionname;

WriteRanch();
RenewDraLog();
CoDataCA();
1;


sub new
{
OutError("bad request") if ($MYRC!=-1);
OutError('�����̗]�T������܂���B') if ($DT->{money} < $RCest);

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

	@RC=reverse(@RC);
	$RCcount++;
	my $i=$RCcount;
	$RC[$i]->{no}=($i > 0) ? ($RC[$i-1]->{no} + 1) : 1 ;
	$RC[$i]->{birth}=$NOW_TIME;
	$RC[$i]->{name}=$Q{name};
	$RC[$i]->{town}=$MYDIR;
	$RC[$i]->{owner}=$DT->{id};
	@RC=reverse(@RC);

WritePayLog($MYDIR,$DT->{id},-$RCest);
PushDraLog(0,"�V�����q��u".$Q{name}."�v���ݗ�����܂����B");
$disp.="�V�����q��u<b>".$Q{name}."</b>�v��ݗ����܂����B";
}


# �M���h�ݗ����� 2004/01/20 �R��

CoLock();
DataRead();
CheckUserPass();
ReadGuild();
ReadGuildData();
$image[0]=GetTagImgKao("�M���h��t","guild");
$Q{er}='gd-f';

$disp.="<BIG>���M���h����</BIG><br><br>";

$Q{url}="http://" if $Q{url} eq "";
$Q{leadt}=$MYDIR;
$Q{leader}=$DT->{id};
@GLIST=(name,shortname,dealrate,feerate,member,comment,appeal,needed,leadt,leader,url);
@MAX=(30,12,4,4,6,30,120,120,10,10,60);
foreach my $i(0..$#GLIST)
	{
	OutError('�L������Ă��Ȃ����ڂ�����܂� - '.$GLIST[$i]) if (!$Q{$GLIST[$i]});
	$Q{$GLIST[$i]}=CutStr(jcode::sjis($Q{$GLIST[$i]},$CHAR_SHIFT_JIS&&'sjis'),$MAX[$i]);
	$Q{$GLIST[$i]}=~s/&/&amp;/g;
	$Q{$GLIST[$i]}=~s/>/&gt;/g;
	$Q{$GLIST[$i]}=~s/</&lt;/g;
	}
$Q{url}="" if $Q{url} eq "http://";
OutError('���⊄�������Ɏg�p�ł��Ȃ��������܂܂�Ă��܂�') if ($Q{dealrate} =~ /([^0-9])/)||($Q{feerate} =~ /([^0-9])/);
OutError('����������10�`500�̊Ԃ̐��l�Ŏw�肵�Ă�������') if ($Q{dealrate} > 500) || ($Q{dealrate} < 10);
OutError('����10�`500�̊Ԃ̐��l�Ŏw�肵�Ă�������') if ($Q{feerate} > 500) || ($Q{feerate} < 10);
OutError('�M���h�R�[�h�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂�') if ($Q{code} =~ /([^a-z])/);
OutError('�M���h�ݗ��ɉ摜�t�@�C���͕K�{�ł�') if (!$Q{upfile})&&($Q{mode} ne "edit");

OutError('�����M���h�R�[�h�����łɑ��݂��Ă��܂�') if (-e $COMMON_DIR."/".$Q{code}.".pl")&&($Q{mode} ne "edit");

GuildImgUp() if ($Q{upfile});
BuildGuild();
CoUnLock();

if ($Q{mode} ne "edit")
{
	Lock();
	DataRead();
	CheckUserPass();
	$DT->{guild}=$Q{code};
	DataWrite();
	DataCommitOrAbort();
	UnLock();
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
�M���h��t�F�葱���������܂����B������ɔ��f�����Ǝv���܂��B<br>
�y�����M���h�ɂȂ��Ă����Ƃ����ł��ˁB�撣���Ă��������B
$TRE$TBE
HTML
OutSkin();
1;


sub GuildImgUp
{
	if ($MIMETYPE{upfile} =~ /gif/i)
	{
	my $ImgFile = $COMMON_DIR."/".$Q{code}.".gif";
	my $upfile=$Q{upfile};
	open(OUT,"> $ImgFile");
	binmode(OUT);
	binmode(STDOUT);
	print OUT $upfile;
	close(OUT);
	chmod (0666,$ImgFile);
	}
	else
	{
	OutError('gif�摜�t�@�C���ł͂Ȃ��悤�ł��B'.$MIMETYPE{upfile});
	}
}

sub BuildGuild
{
	my @MESSAGE=();
	push(@GLIST, @OtherDir);
	foreach my $i(0..$#GLIST)
		{
		$MESSAGE[$i]=$GLIST[$i]."=".$Q{$GLIST[$i]}."\n";
		}
	OpenAndCheck($COMMON_DIR."/".$Q{code}.".pl");
	print OUT @MESSAGE;
	close(OUT);
}


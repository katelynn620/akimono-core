# wis 2004/02/28 �R��

$image[0]=GetTagImgKao("����`��","help");
DataRead();
CheckUserPass();
$disp.="<BIG>��wis</BIG><br><br>";

if ($Q{form})
{
WisWrite();
}
else
{
WisForm();
}
OutSkin();
1;


sub WisForm
{
	$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F����ɘb�������邱�Ƃ��ł��܂���B<br>
���ꂮ�������̂Ȃ��悤�ɂ��Ă��������B
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
$TB
$TR$TDB<b>����</b>
HTML

$disp.=$TD."<SELECT NAME=to><OPTION VALUE=\"-1\">�|�|����I���|�|";
	foreach (@DT)
	{
		$disp.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
	}
$disp.="</SELECT>$TRE\n";

$disp.=<<"HTML";
$TR$TDB<b>���e</b>
$TD<INPUT TYPE=TEXT NAME=msg SIZE=60>$TRE
$TR$TD<SPAN>�g�p�@</SPAN>$TD
�E���肪��M����O�ɕʂ�wis��������ƁC�ŏ���wis�͏����Ă��܂��܂��B<br>
�E���肪���O�C�����Ă��Ȃ��ꍇ�C��ɂȂ��Ď�M����邱�Ƃ�����܂��B<br>
�E�`���b�g����Ɏg���͔̂����܂��傤�B
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="plus">
<INPUT TYPE=SUBMIT VALUE="���M">
</FORM>
HTML
}

sub WisWrite
{
	my ($to,$msg)=($Q{to},$Q{msg});
	OutError("������w�肵�Ă��������B") if $to==-1;
	OutError("���݂��Ȃ��X�܂ł��B") if !defined($id2idx{$to});
	OutError("���b�Z�[�W����͂��Ă��������B") if !$msg;
	OutError('���b�Z�[�W�̕������������ł��B') if length($msg)>72;
	$NOMENU=1;$Q{bk}="wis";
	$msg=~s/&/&amp;/g;
	$msg=~s/>/&gt;/g;
	$msg=~s/</&lt;/g;
	OpenAndCheck(GetPath($SUBDATA_DIR,$DT[$id2idx{$to}]->{id}."-wis"));
	print OUT "<SPAN>$DT->{name}</SPAN> > <b>$msg</b>";
	close(OUT);
	$disp.="wis���M���܂����B";
	return;
}


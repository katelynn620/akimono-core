# �t�H�[���\�� 2004/01/20 �R��

$disp.=GetMenuTag('letter','[��M��]')
	.GetMenuTag('letter','[���M��]','&old=list')
	."<b>[�莆������]</b>";
$disp.="<hr width=500 noshade size=1>";
my $cnt=$MAX_BOX - scalar(@SENLETTER);
if ($cnt > 0)
{
$preerror="";
LFormCheck() if ($Q{form} eq 'check');
NewLform() if ($preerror || $Q{form} eq 'make');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F����ȏ�̎莆�𑗂邱�Ƃ͂ł��܂���B<br>
���M�ς݂̎莆���폜���Ă��������B
$TRE$TBE
HTML

}


1;

sub NewLform
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F���� $cnt�ʂ܂Ŏ莆�𑗂邱�Ƃ��ł��܂��B<br>
�}�i�[�����C���炤����̐l�̂��Ƃ��l���ď����܂��傤�B
$TRE$TBE<br>$preerror
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>����</b>�i�����ꂩ�P�j
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"-1\">����I��";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($Q{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE
$TR$TDB<b>�^�C�g��</b>�i40���ȓ��j
<td colspan=2><INPUT TYPE=TEXT NAME=title SIZE=40 VALUE="$Q{title}">$TRE
$TR$TDB<b>���e</b>�i400���ȓ��j
<td colspan=2><INPUT TYPE=TEXT NAME=msg SIZE=60 VALUE="$Q{msg}">$TRE
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="check">
<INPUT TYPE=SUBMIT VALUE="���M�m�F">
</FORM>
HTML
}

sub LFormCheck
{
my $sendmail="";
my $sendto="";
foreach my $pg(@OtherDir)
	{
	$sendmail=$Q{$pg}, $sendto=$pg if ($Q{$pg} != -1)
	}
$preerror="������w�肵�Ă��������B", return if !$sendto;
my $Ln=SearchLetterName($sendmail,$sendto);
$preerror="���݂��Ȃ��X�܂ł��B", return if ($Ln == -1);
$preerror="���b�Z�[�W���L�����Ă��������B", return if (!$Q{msg});
$Q{title}="�i����j" if !$Q{title};
$preerror='�^�C�g���͔��p40��(�S�p20��)�܂łł��B���ݔ��p'.length($Q{title}).'���ł��B', return if length($Q{title})>40;
$preerror='���e���͔��p400����(�S�p200����)�܂łł��B���ݔ��p'.length($Q{msg}).'�����ł��B', return if length($Q{msg})>400;

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
����`���F�ȉ��̓��e�Ŏ莆�𑗂�܂��B<br>
����ł�낵�������m�F���������B
$TRE$TBE<br>
<table width=60%>$TR$TD
<SPAN>����</SPAN>�F$Ln <small>�i$Tname{$sendto}�j</small><br>
<SPAN>�^�C�g��</SPAN>�F�u$Q{title}�v<br>
<SPAN>���e</SPAN>�F$Q{msg}<br>
$TRE$TBE
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=$sendto VALUE="$sendmail">
<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
<INPUT TYPE=HIDDEN NAME=form VALUE="make">
<INPUT TYPE=SUBMIT NAME=ok VALUE="���M">
<INPUT TYPE=SUBMIT NAME=ng VALUE="�ĕҏW">
</FORM>
HTML
}

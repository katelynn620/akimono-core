# ��M���X�g�\�� 2004/01/20 �R��

if ($Q{old})
{
LetterSending();
}
else
{
LetterReading();
}
1;

sub LetterReading
{
$disp.="<b>[��M��]</b> "
	.GetMenuTag('letter','[���M��]','&old=list')
	.GetMenuTag('letter',		'[�莆������]','&form=make');
$disp.="<hr width=500 noshade size=1>";
my $cnt=scalar(@RECLETTER);
my $boxlimit=GetTime2HMS($BOX_STOCK_TIME);

if (!$cnt)
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F���ݓ͂��Ă���莆�͂���܂���B<br>
�莆�� $boxlimit�߂���Ɩ����Ȃ�܂��̂ŋC�����Ă��������B
$TRE$TBE
HTML
return;
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F���� $cnt�ʂ̎莆���͂��Ă���C���� $NeverR�ʂ����ǂł��B<br>
�莆�� $boxlimit�߂���Ɩ����Ȃ�܂��̂ŋC�����Ă��������B
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
HTML

foreach my $i(@RECLETTER)
	{
	my $sname=SearchLetterName($LETTER[$i]->{fromid},$LETTER[$i]->{fromt});
	$disp.="<input type=checkbox name=\"del_".$LETTER[$i]->{no}."\" value=\"1\">";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>����</SPAN>�F" : "��M�F";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." �c from�F<span>".$sname."</span>";
	$disp.=" <small>�i".$Tname{$LETTER[$i]->{fromt}}."�j</small> ";
	$disp.="<a href=\"action.cgi?key=letter&$USERPASSURL&form=make&";
	$disp.=$LETTER[$i]->{fromt}."=".$LETTER[$i]->{fromid}."\">[�ԐM]</a><br>";
	$disp.="<table width=60%><tr><td>";
	$disp.="�u".$LETTER[$i]->{title}."�v<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	$LETTER[$i]->{mode}=0, $WriteFlag=1 if ($LETTER[$i]->{mode}==1);	#���ǂ����ǂɁB
	$LETTER[$i]->{mode}=2 if ($LETTER[$i]->{fromid}==1);			#��z�֒ʒm�͍폜�B
	}
$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="�I�������莆���폜">
</FORM>
HTML
}

sub LetterSending
{
$disp.=GetMenuTag('letter','[��M��]')
	."<b>[���M��]</b> "
	.GetMenuTag('letter',		'[�莆������]','&form=make');
$disp.="<hr width=500 noshade size=1>";
my $cnt=scalar(@SENLETTER);

if (!$cnt)
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F���ݑ����Ă���莆�͂���܂���B<br>
�莆�͍��v $MAX_BOX�ʂ܂ő��邱�Ƃ��ł��܂��B
$TRE$TBE
HTML
return;
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>����`��</SPAN>�F���݂܂ő������莆�� $cnt�ʂł��B<br>
���̂������肪�ǂ�ł��Ȃ��莆�� $NeverS�ʂ���܂��B
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
<INPUT TYPE=HIDDEN NAME=old VALUE="list">
HTML

foreach my $i(@SENLETTER)
	{
	my $sname=SearchLetterName($LETTER[$i]->{toid},$LETTER[$i]->{tot});
	$sname="(�s��)" if $sname eq "-1";
	$disp.="<input type=checkbox name=\"del_".$LETTER[$i]->{no}."\" value=\"1\">";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>����</SPAN>�F" : "���M�F";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." �c to�F<span>".$sname."</span>";
	$disp.=" <small>�i".$Tname{$LETTER[$i]->{tot}}."�j</small><BR>";
	$disp.="<table width=60%><tr><td>";
	$disp.="�u".$LETTER[$i]->{title}."�v<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	}
$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="�I�������莆���폜">
<br>�i����̂Ƃ��납����폜����܂��j
</FORM>
HTML
}

use utf8;
# 受信リスト表示 2004/01/20 由來

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
$disp.="<b>[".l('受信箱')."]</b> "
	.GetMenuTag('letter','['.l('送信箱').']','&old=list')
	.GetMenuTag('letter',		'['.l('手紙を書く').']','&form=make');
$disp.="<hr width=500 noshade size=1>";
my $cnt=scalar(@RECLETTER);
my $boxlimit=GetTime2HMS($BOX_STOCK_TIME);

if (!$cnt)
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l("お手伝い")}</SPAN>：${\l("現在届いている手紙はありません。")}<br>
${\l("手紙は%1過ぎると無くなりますので気をつけてください。",$boxlimit)}
$TRE$TBE
HTML
return;
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l("お手伝い")}</SPAN>：${\l("現在 %1通の手紙が届いており，うち %2通が未読です。",$cnt,$NeverR)}<br>
${\l("手紙は%1過ぎると無くなりますので気をつけてください。",$boxlimit)}
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
HTML

foreach my $i(@RECLETTER)
	{
	my $sname=SearchLetterName($LETTER[$i]->{fromid},$LETTER[$i]->{fromt});
	$disp.="<input type=checkbox name=\"del_".$LETTER[$i]->{no}."\" value=\"1\">";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>".l('未読')."</SPAN>：" : l('受信')."：";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." … from：<span>".$sname."</span>";
	$disp.=" <small>（".$Tname{$LETTER[$i]->{fromt}}."）</small> ";
	$disp.="<a href=\"action.cgi?key=letter&$USERPASSURL&form=make&";
	$disp.=$LETTER[$i]->{fromt}."=".$LETTER[$i]->{fromid}."\">[".l('返信')."]</a><br>";
	$disp.="<table width=60%><tr><td>";
	$disp.="「".$LETTER[$i]->{title}."」<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	$LETTER[$i]->{mode}=0, $WriteFlag=1 if ($LETTER[$i]->{mode}==1);	#未読を既読に。
	$LETTER[$i]->{mode}=2 if ($LETTER[$i]->{fromid}==1);			#宅配便通知は削除。
	}
$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="${\l('選択した手紙を削除')}">
</FORM>
HTML
}

sub LetterSending
{
$disp.=GetMenuTag('letter','['.l('受信箱').']')
	."<b>[".l('送信箱')."]</b> "
	.GetMenuTag('letter',		'['.l('手紙を書く').']','&form=make');
$disp.="<hr width=500 noshade size=1>";
my $cnt=scalar(@SENLETTER);

if (!$cnt)
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l("お手伝い")}</SPAN>：${\l('現在送っている手紙はありません。')}<br>
${\l("手紙は合計 %1通まで送ることができます。",$MAX_BOX)}
$TRE$TBE
HTML
return;
}

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l("お手伝い")}</SPAN>：${\l('現在まで送った手紙は %1通です。',$cnt)}<br>
${\l('このうち相手が読んでいない手紙は %1通あります。',$NeverS)}
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
<INPUT TYPE=HIDDEN NAME=old VALUE="list">
HTML

foreach my $i(@SENLETTER)
	{
	my $sname=SearchLetterName($LETTER[$i]->{toid},$LETTER[$i]->{tot});
	$sname="(".l('不明').")" if $sname eq "-1";
	$disp.="<input type=checkbox name=\"del_".$LETTER[$i]->{no}."\" value=\"1\">";
	$disp.=($LETTER[$i]->{mode}==1) ? "<SPAN>".l('未読')."</SPAN>：" : "".l('送信')."：";
	$disp.=GetTime2FormatTime($LETTER[$i]->{time})." … to：<span>".$sname."</span>";
	$disp.=" <small>（".$Tname{$LETTER[$i]->{tot}}."）</small><BR>";
	$disp.="<table width=60%><tr><td>";
	$disp.="「".$LETTER[$i]->{title}."」<BR>";
	$disp.=$LETTER[$i]->{msg}."<BR>";
	$disp.="</td></tr></table><hr width=500 noshade size=1>";
	}
$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="${\l('選択した手紙を削除')}">
<br>（${\l('相手のところからも削除されます')}）
</FORM>
HTML
}

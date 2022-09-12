use utf8;
# フォーム表示 2004/01/20 由來

$disp.=GetMenuTag('letter','['.l('受信箱').']')
	.GetMenuTag('letter','['.l('送信箱').']','&old=list')
	."<b>[".l('手紙を書く')."]</b>";
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
<SPAN>${\l("お手伝い")}</SPAN>：${\l("これ以上の手紙を送ることはできません。")}<br>
${\l("送信済みの手紙を削除してください。")}
$TRE$TBE
HTML

}


1;

sub NewLform
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l("お手伝い")}</SPAN>：${\l("あと %1通まで手紙を送ることができます。",$cnt)}<br>
${\l("マナーを守り，もらう立場の人のことを考えて書きましょう。")}
$TRE$TBE<br>$preerror
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>${\l("宛先")}</b>${\l("（いずれか１つ）")}
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"-1\">宛先選択";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($Q{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE
$TR$TDB<b>${\l("タイトル")}</b>${\l("（40字以内）")}
<td colspan=2><INPUT TYPE=TEXT NAME=title SIZE=40 VALUE="$Q{title}">$TRE
$TR$TDB<b>${\l('内容')}</b>${\l("（400字以内）")}
<td colspan=2><INPUT TYPE=TEXT NAME=msg SIZE=60 VALUE="$Q{msg}">$TRE
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="check">
<INPUT TYPE=SUBMIT VALUE="${\l('送信確認')}">
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
$preerror=l("宛先を指定してください。"), return if !$sendto;
my $Ln=SearchLetterName($sendmail,$sendto);
$preerror=l("存在しない店舗です。"), return if ($Ln == -1);
$preerror=l("メッセージを記入してください。"), return if (!$Q{msg});
$Q{title}=l("（無題）") if !$Q{title};
$preerror=l('タイトルは半角40字(全角20字)までです。現在半角%1字です。',length($Q{title})), return if length($Q{title})>40;
$preerror=l('内容文は半角400文字(全角200文字)までです。現在半角%1文字です。',length($Q{msg})), return if length($Q{msg})>400;

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
${\l("お手伝い")}：${\l("以下の内容で手紙を送ります。")}<br>
${\l("これでよろしいかご確認ください。")}
$TRE$TBE<br>
<table width=60%>$TR$TD
<SPAN>${\l("宛先")}</SPAN>：$Ln <small>（$Tname{$sendto}）</small><br>
<SPAN>${\l("タイトル")}</SPAN>：「$Q{title}」<br>
<SPAN>${\l("内容")}</SPAN>：$Q{msg}<br>
$TRE$TBE
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=$sendto VALUE="$sendmail">
<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
<INPUT TYPE=HIDDEN NAME=form VALUE="make">
<INPUT TYPE=SUBMIT NAME=ok VALUE="${\l('送信')}">
<INPUT TYPE=SUBMIT NAME=ng VALUE="${\l('再編集')}">
</FORM>
HTML
}

use utf8;
# wis 2004/02/28 由來

$image[0]=GetTagImgKao(l("お手伝い"),"help");
DataRead();
CheckUserPass();
$disp.="<BIG>●".l("wis")."</BIG><br><br>";

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
<SPAN>${\l('お手伝い')}</SPAN>：${\l('相手に話しかけることができますよ。')}<br>
${\l('くれぐれも失礼のないようにしてください。')}
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
$TB
$TR$TDB<b>${\l('相手')}</b>
HTML

$disp.=$TD."<SELECT NAME=to><OPTION VALUE=\"-1\">".l('－－相手選択－－');
	foreach (@DT)
	{
		$disp.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
	}
$disp.="</SELECT>$TRE\n";

$disp.=<<"HTML";
$TR$TDB<b>${\l('内容')}</b>
$TD<INPUT TYPE=TEXT NAME=msg SIZE=60>$TRE
$TR$TD<SPAN>${\l('使用法')}</SPAN>$TD
${\l('・相手が受信する前に別なwisが送られると，最初のwisは消えてしまいます。')}<br>
${\l('・相手がログインしていない場合，後になって受信されることがあります。')}<br>
${\l('・チャット代わりに使うのは避けましょう。')}
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="plus">
<INPUT TYPE=SUBMIT VALUE="${\l('送信')}">
</FORM>
HTML
}

sub WisWrite
{
	my ($to,$msg)=($Q{to},$Q{msg});
	OutError(l('相手を指定してください。')) if $to==-1;
	OutError(l('存在しない店舗です。')) if !defined($id2idx{$to});
	OutError(l('メッセージを入力してください。')) if !$msg;
	OutError(l('メッセージの文字数が多いです。')) if length($msg)>72;
	$NOMENU=1;$Q{bk}="wis";
	$msg=~s/&/&amp;/g;
	$msg=~s/>/&gt;/g;
	$msg=~s/</&lt;/g;
	OpenAndCheck(GetPath($SUBDATA_DIR,$DT[$id2idx{$to}]->{id}."-wis"));
	print OUT "<SPAN>$DT->{name}</SPAN> > <b>$msg</b>";
	close(OUT);
	$disp.=l("wis送信しました。");
	return;
}


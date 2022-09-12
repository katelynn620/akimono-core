use utf8;
# 住宅一覧表示 2005/03/30 由來

if ($Q{form} eq "pro" && !$GUEST_USER)
{
ProposeForm();
}
elsif ($Q{form} && !$GUEST_USER)
{
ConstForm();
}
else
{
BrideList();
}
1;

sub BrideList
{
my $i;
if (!$GUEST_USER && !$married)
{
$i="<br><a href=\"action.cgi?key=bride&form=pro&$USERPASSURL\">[".l('プロポーズする')."]</a>";
}

$disp.=<<STR;
$TBT$TRT$TD
<IMG width="96" height="192" SRC="$IMAGE_URL/map/church.png"><td width=10>$TD
$image[3]
<SPAN>${\l('神父')}</SPAN><br>
${\l('結婚についてご存知ですか？')}<br>
${\l('結婚して住宅を建てると，そこに持ち物を置くことができるのですよ。')}<br>
${\l('住宅を持つまでの間は，この教会の持ち物置き場を使ってかまいません。')}<br>
${\l('でも大事なのは，やはり二人の強い絆でしょうね。')}$i
$TRE$TBE<br>
$TB$TR
$TDB${\l('点数')}
$TDB${\l('状態')}
$TDB${\l('詳細')}
$TDB${\l('日数')}
$TDB${\l('保管品')}
$TRE
STR
@BRIDE=sort{$b->{point}<=>$a->{point}}@BRIDE;
foreach my $i(0..$Scount) {
	next if ($BRIDE[$i]->{mode}==-1) || !defined($BRIDE[$i]->{no});
	my ($ida,$idb)=($BRIDE[$i]->{ida},$BRIDE[$i]->{idb});
	$disp.=($DT->{id} == $ida || $DT->{id} == $idb) ? $TR.$TDB : $TR.$TD;
	$disp.='<b>No.'.($i+1).'</b><br>'.$BRIDE[$i]->{point}.'<td>';
	$disp.=    "<a href=\"action.cgi?key=bride&no=$BRIDE[$i]->{no}&$USERPASSURL\">" if (!$GUEST_USER);

	if (!$BRIDE[$i]->{mode})
	{
	$disp.=$image[2];
	$disp.=    "</a>" if (!$GUEST_USER);
	$disp.='<td>'.l('%1 から <SPAN>%2</SPAN> へ',$DT[$id2idx{$ida}]->{shopname},$DT[$id2idx{$idb}]->{shopname});
	}
	else
	{
	$disp.=($BRIDE[$i]->{mode}==1)?$image[0]:$image[1];
	$disp.=    "</a>" if (!$GUEST_USER);
	$disp.='<td>'.$DT[$id2idx{$ida}]->{shopname}.' ＆ '.$DT[$id2idx{$idb}]->{shopname};
	}
	$disp.="<td align=center>".GetTime2found($NOW_TIME-$BRIDE[$i]->{tm});
	$disp.='<td>'.GetMoneyMessage($BRIDE[$i]->{money}).'<br>';
	foreach (0..$BRIDE[$i]->{mode}-1) { $disp.=GetTagImgItemType($BRIDE[$i]->{stock}[$_]);}
	}
$disp.=$TRE.$TBE;
}

sub ProposeForm
{
	OutError('bad request') if $married;
	$userselect="";
	foreach my $DTS (@DT)
	{
		$userselect.="<OPTION VALUE=\"$DTS->{id}\">$DTS->{name} ($DTS->{shopname})";
	}
$disp.=<<STR;
$TB$TR$TD
$image[3]
${\l('神父')}：${\l('家族を持つことをお望みですか？ それなら次の注意をよく聴いてください。')}<br>
・${\l('お互いに結婚資金が<b>500万%1</b>かかります。',$term[2])}<br>
・${\l('結婚相手は慎重に選びなさい。その人と助け合っていけるかよく考えるのです。')}<br>
・${\l('事前によく話し合いなさい。とつぜんプロポーズをしても相手は困るでしょう。')}<br>
・${\l('プロポーズをした側が夫となり，受けた側が妻になります。')}
$TRE$TBE<br>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="new">
<BIG>●${\l('プロポーズ')}</BIG>：${\l('私 %1 (%2)は',$DT->{name},$DT->{shopname})}
<SELECT NAME=tg>$userselect</SELECT>
${\l('を妻とし')}<br>
${\l('健やかなる時も病める時もその身を共にする事を')}
<INPUT TYPE=SUBMIT VALUE='${\l('誓います')}'>
</FORM>
STR
}

sub ConstForm
{
$disp.=<<STR;
$TB$TR$TD
$image[3]
${\l('神父')}：${\l('住宅を建てるのですか？ それなら次の注意をよく聴いてください。')}<br>
・${\l('資金が<b>1500万%1</b>かかります。共用倉庫から支出されます。',$term[2])}<br>
・${\l('一度建てたら場所を移ることはできません。')}<br>
$TRE$TBE
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="con">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$Q{idx}">
<INPUT TYPE=HIDDEN NAME=place VALUE="$Q{form}">
<BIG>●${\l('住宅建築')}</BIG>：${\l('指定の場所に住宅を')}
<INPUT TYPE=SUBMIT VALUE='${\l('建築する')}'>
</FORM>
STR
}

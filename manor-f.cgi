use utf8;
# 荘園管理 2005/03/30 由來

Lock() if $Q{mode};
$image[0]=GetTagImgKao(l("大臣"),"minister",'align="left" ');
DataRead();
CheckUserPass();
OutError(l('荘園管理を行えるのは領主のみです')) if $STATE->{leader}!=$DT->{id};
RequireFile('inc-manor.cgi');

ReadDTSub($DT,"lord");
my $functionname=$Q{mode};
&$functionname if defined(&$functionname);


# 荘園設定を取得
my $MANORLORD=$DT->{_lord};

my $shoplist="";
my $taxsum=0;
foreach (@DT) {
$shoplist.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
$taxsum+=$_->{taxtoday};
}

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $ii=($now % $ONE_DAY_TIME);
$ii=1 if $ii < 1;
$taxsum=GetMoneyString(int($taxsum * $ONE_DAY_TIME / $ii / 10000) * 10000);

$disp.="<BIG>●".l("荘園管理室")."</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0]."<SPAN>".l("大臣")."</SPAN>：".l("財政状態に気をつけて運営しないといけませんぞ。")."<br>";
$disp.="・".l("販売在庫は，一度につき 1000個まで。")."<br>";
$disp.="・".l("種の販売価格は，%1 ～ %2。",GetMoneyString(1000),GetMoneyString(10000))."<br>";
$disp.="・".l("収穫物の買取価格は，%1 ～ %2",GetMoneyString(5000),GetMoneyString(40000))."。<br>";
$disp.="・".l("販売価格を買取価格より高くすると，誰も使いたがりませんのでご注意を。").$TRE.$TBE;

$disp.="<hr width=500 noshade size=1><BIG>●".l("現在の財政状態")."</BIG><br><br>";
$disp.="$TB$TDB".l("街資金")."$TDB".l("税収見込み")."$TDB".l("前期税収")."$TDB".l("前期歳出")."$TRE";
$disp.=$TR.$TD.GetMoneyString($STATE->{money}).$TD.$taxsum;
$disp.=$TD.GetMoneyString($STATE->{in}).$TD.GetMoneyString($STATE->{out}).$TRE.$TBE;


$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>●${\l('荘園設定')}</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="inside">
$TB$TR
$TDB${\l('種')}$TDB${\l('販売在庫')}$TDB${\l('販売価格')}$TD$TDB${\l('収穫物')}$TDB${\l('買取価格')}$TDB${\l('買取った数')}$TDB${\l('説明')}$TRE
HTML

my $balance=0;
foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	$disp.=$TR.$TD.GetTagImgManor($MYMANOR[1]).$MYMANOR[0];
	my $c=$MANORLORD->{"count$i"} + 0;
	$disp.=qq|$TD<INPUT TYPE=TEXT NAME=count$i SIZE=8 VALUE="$c"> ${\l('個')}|;
	my $t=$MANORLORD->{"price$i"} + 0;
	$balance-=$c*$t;
	$disp.=$TD."@".qq|$term[0]<INPUT TYPE=TEXT NAME=price$i SIZE=8 VALUE="$t">$term[1]|;
	$disp.=$TD."→".$TD.GetTagImgManor($MYMANOR[3]).$MYMANOR[2];
	$t=$MANORLORD->{"cost$i"} + 0;
	$balance+=$c*$t;
	$disp.=$TD."@".qq|$term[0]<INPUT TYPE=TEXT NAME=cost$i SIZE=8 VALUE="$t">$term[1]|;
	$disp.=$TD.($MANORLORD->{"stock$i"} +0)." ".l("個");
	$disp.=$TD."<small>".l("買取数 %1個で%2%3を生成",$MYMANOR[5],GetTagImgItemType($MYMANOR[4]),$ITEM[$MYMANOR[4]]->{name})."</small>".$TRE;
	}
$disp.=$TBE."<br>※".l("上記の荘園設定では，%1の財政支出が見込まれます。",GetMoneyString($balance))."<br><br>";

$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="${\l('以上の内容で決定')}">
</FORM>
<hr width=500 noshade size=1>
	<FORM ACTION="action.cgi" $METHOD>
	$MYFORM$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outside">
<BIG>●${\l('産物生成')}</BIG>： ${\l('買い取った収穫物から産物を ')}
<INPUT TYPE=SUBMIT VALUE="${\l('生成する')}">
	</FORM>
HTML

OutSkin();
1;


sub inside
{
foreach my $i(0..$#MANOR)
	{
	$DT->{_lord}->{"count$i"}=CheckCount($Q{"count$i"},0,0,1000);
	$DT->{_lord}->{"price$i"}=CheckCount($Q{"price$i"},0,1000,10000);
	$DT->{_lord}->{"cost$i"}=CheckCount($Q{"cost$i"},0,5000,40000);
	}
WriteDTSub($DT,"lord");
DataCommitOrAbort();
UnLock();
}

sub outside
{
my $flag=0;
foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	my $num=0;
	$num=int($DT->{_lord}->{"stock$i"} / $MYMANOR[5]) if $MYMANOR[5];
	next if !$num;	#生成可能数なし

	my $itemno=$MYMANOR[4];
	my $count=CheckCount($num,0,0,$ITEM[$itemno]->{limit} - $DT->{item}[$itemno-1]);
	$disp.=l("%1は倉庫にいっぱいなので生成をとりやめました。",$ITEM[$itemno]->{name})."<br>" , next if !$count;

	$flag++;
	$DT->{item}[$itemno-1]+=$count;
	$DT->{_lord}->{"stock$i"}-=$count * $MYMANOR[5];
	$disp.=l("%1を%2%3生成しました。",$ITEM[$itemno]->{name},$count,$ITEM[$itemno]->{scale})."<br>";
	PushLog(0,l("%1荘園にて%2を%3%4生成",$DT->{id},$ITEM[$itemno]->{name},$count,$ITEM[$itemno]->{scale}));
	}

if ($flag)
	{
	WriteDTSub($DT,"lord");
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	}
	else
	{
	$disp.=l('生成可能なものがありませんでした。');
	}
UnLock();
OutSkin();
exit;
}






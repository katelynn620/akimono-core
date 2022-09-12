use utf8;
# 兵士雇用反乱処理 2005/01/06 由來

$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
ReadArmy();

my $functionname=$Q{mode};
OutError('bad request') if !defined(&$functionname);
&$functionname;

WriteArmy();
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('army',	'['.l('傭兵所へ').']');
$disp.=GetMenuTag('main','['.l('自店に戻る').']');
$disp.=$TRE.$TBE;
$disp.="<br>".$ret;
OutSkin();
1;


sub plus
{
my $limit=($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
my $price=($DTevent{rebel}) ? 1500 : 1000;
my $usetime=60*40;
UseTime($usetime);

$num=CheckCount($Q{cnt1},$Q{cnt2},0,$limit);
OutError(l('数量を指定してください。')) if !$num;

$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;
OutError(l('資金が足りません。')) if !$num;

$ARMY{$DT->{id}}+=$num;
$DT->{money}-=$num*$price;

$ret=l("兵士駐屯所にてドワーフ兵士を%1人@%2(計%3)にて雇いました",$num,GetMoneyString($price),GetMoneyString($price*$num));
$ret.="/".l("%1消費",GetTime2HMS($usetime));
PushLog(0,$DT->{id},$ret);
}

sub fire
{
$num=CheckCount($Q{cnt1},$Q{cnt2},0,$ARMY{$DT->{id}});
OutError(l('数量を指定してください。')) if !$num;

my $usetime=60*10;
UseTime($usetime);
$ARMY{$DT->{id}}-=$num;

$ret=l("ドワーフ兵士を%1人解雇しました",$num);
$ret.="/".l("%1消費",GetTime2HMS($usetime));
PushLog(0,$DT->{id},$ret);
}

sub rebelon
{
OutError(l('反乱を開始するには rebel と入力してください。')) if ($Q{cmd} ne "rebel");
OutError(l('兵士数が足りません。')) if ($ARMY{$DT->{id}} < 2500);

my $usetime=60*30;
UseTime($usetime);
$DTevent{rebel}=$NOW_TIME+86400*3;
$RIOT{$DT->{id}}=1;
$STATE->{safety}=int($STATE->{safety} * 9 / 10) if ($STATE->{safety} > 5000);

$ret=l("ドワーフ兵士が武装蜂起。反乱が始まりました！");
PushLog(2,0,l("%1の指揮で%2",$DT->{shopname},$ret));
$ret.="/".l("%1消費",GetTime2HMS($usetime));
}

sub rside
{
OutError(l('反乱に呼応するには rebel と入力してください。')) if ($Q{cmd} ne "rebel");

my $usetime=60*20;
UseTime($usetime);
$RIOT{$DT->{id}}=1;

$ret=l("反乱に呼応し，参戦しました！");
PushLog(3,0,l("%1が%2",$DT->{shopname},$ret));
$ret.="/".l("%1消費",GetTime2HMS($usetime));
}

sub lside
{
OutError(l('反乱に参加しながら領主の味方をすることはできません。')) if ($RIOT{$DT->{id}});

my $usetime=60*20;
UseTime($usetime);
if ($STATE->{leader}==$DT->{id})
	{
	$STATE->{army}+=$ARMY{$DT->{id}};
	}
	else
	{
	$STATE->{robina}+=$ARMY{$DT->{id}};
	PushLog(3,0,l('%1は領主に味方し，義勇兵を派遣しました。',$DT->{shopname}));
	}

delete $ARMY{$DT->{id}};
$ret=l("兵士を領主の護衛軍に派遣しました");
$ret.="/".l("%1消費",GetTime2HMS($usetime));
}

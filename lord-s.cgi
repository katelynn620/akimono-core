use utf8;
# 領主邸 2004/01/20 由來

$image[0]=GetTagImgKao(l("大臣"),"minister");
Lock();
DataRead();
CheckUserPass();

my $functionname=$Q{mode};
OutError('bad request') if !defined(&$functionname);
&$functionname;
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;

sub inside
{
if ($Q{taxrate} =~ /([^0-9])/
	|| $Q{devem} =~ /([^0-9])/
	|| $Q{safem} =~ /([^0-9])/
	) { OutError(l('使用できる文字は半角数字だけです')); }
OutError($image[0].l('いくら何でもそれは高すぎというものですぞ。')) if ($Q{taxrate} > 40) ;
OutError($image[0].l('一度にそれだけ対策費をつぎこんでも無意味ですぞ。')) if ($Q{devem} > 10000000 || $Q{safem} > 10000000) ;

$Q{taxrate}=0 if $Q{taxrate}<0;
$Q{devem}=0 if $Q{devem}<0;
$Q{safem}=0 if $Q{safem}<0;
my $taxrate=int($Q{taxrate});
$disp.=l("街の内政方針を変更しました。");

if ($DTTaxrate != $taxrate )
	{
	my $i=l("引き上げました");
	$i="引き下げました" if $DTTaxrate > $taxrate;
	$DTTaxrate=int($Q{taxrate});
	PushLog(2,0,l("領主%1は街の税率を%2%に%3。",$DT->{name},$taxrate,$i));
	$disp.="<br>".l("街の税率を%1%に%2。",$taxrate,$i);
	}
$STATE->{devem}=int($Q{devem});
$STATE->{safem}=int($Q{safem});
}

sub outside
{
OutError(l('反乱中のため雇用できません。')) if $DTevent{rebel};
my $stock=int($STATE->{money} / 1200);
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$stock);
OutError(l('雇用人数を指定してください')) if !$count;
$STATE->{money}-=$count * 1200;
$STATE->{army}+=$count;
$disp.=l("護衛軍を%1人雇いました。",$count);
}

sub outdel
{
OutError(l('反乱中のため解雇できません。')) if $DTevent{rebel};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$STATE->{army});
OutError(l('解雇人数を指定してください')) if !$count;
$STATE->{army}-=$count;
$disp.=l("護衛軍を%1人解雇しました。",$count);
}

sub taxside
{
OutError(l('対象店を選択してください。')) if !defined($id2idx{$Q{tg}});
my $i=$id2idx{$Q{tg}};
if ($Q{md} eq "free")
	{
	PushLog(2,0,"領主%1は%2の税を免除しました。",$DT->{name},$DT[$i]->{shopname}) if ($DT[$i]->{taxmode}!=1);
	$DT[$i]->{taxmode}=1;
	$disp.=l("%1の税を免除しました。",$DT[$i]->{shopname});
	}
elsif ($Q{md} eq "double")
	{
	PushLog(2,0,"領主%1は%2の税率を倍にしました。",$DT->{name},$DT[$i]->{shopname}) if ($DT[$i]->{taxmode}!=2);
	$DT[$i]->{taxmode}=2;
	$disp.=l("%1の税率を倍にしました。",$DT[$i]->{shopname});
	}
	else
	{
	PushLog(2,0,"領主%1は%2の免税を取りやめました。",$DT->{name},$DT[$i]->{shopname}) if ($DT[$i]->{taxmode}==1);
	PushLog(2,0,"領主%1は%2の倍税を取りやめました。",$DT->{name},$DT[$i]->{shopname}) if ($DT[$i]->{taxmode}==2);
	delete $DT[$i]->{taxmode};
	$disp.=l("%1の税を通常に戻しました。",$DT[$i]->{shopname});
	}
}

sub treset
{
foreach (@DT) {
	delete $_->{taxmode};
}
PushLog(2,0,l("領主%1は倍税や免税をすべて取りやめました。",$DT->{name}));
$disp.=l("全ての店の税率を通常に戻しました。");
}

sub expose
{
OutError(l('反乱中のため実行できません。')) if $DTevent{rebel};
OutError(l('対象店を選択してください。')) if !defined($id2idx{$Q{tg}});
OutError(l('費用が足りません。')) if ($STATE->{money} < 1000000);
my $i=$id2idx{$Q{tg}};
OutError($image[0].l('その店舗に対する取り締まりはあまり意味がないようですぞ。')) if ($DT[$i]->{rank} < 2000) ;
$STATE->{money}-=1000000;
$DT[$i]->{rank}=int($DT[$i]->{rank} / 10);
$STATE->{safety}+=500;
$STATE->{safety}=10000 if $STATE->{safety} > 10000;
PushLog(2,0,l("領主%1は%2に対して取り締まりを行いました。",$DT->{name},$DT[$i]->{shopname}));
$disp.=l("%1に対して取り締まりを行いました。",$DT[$i]->{shopname});
}


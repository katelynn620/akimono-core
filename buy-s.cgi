# �w������ 2005/03/30 �R��

$NOMENU=1;
$id=int($Q{id}+0);
$showcase=int($Q{sc}+0);
$itemno=int($Q{it}+0);
$price=int($Q{pr}+0);
$Q{er}=(($id==0)?'shop-m':'shop-a');

Lock();
DataRead();
CheckUserPass();

$num=CheckCount($Q{num1},$Q{num2},0,$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1]);
OutError('���ʂ��w�肵�Ă��������B') if !$num;

if($id==0)
{
	# �s��
	$DTS=GetWholeStore();
	$DTS->{_wholestore_}=1;
}
else
{
	# ��ʓX
	OutError('�X�I��������������܂���') if !defined($id2idx{$id});
	$DTS=$DT[$id2idx{$id}];
}
OutError('�����̓X���甃�����Ƃ͂ł��܂���') if $DT->{id}==$DTS->{id};
CheckShowCaseNumber($DTS,$showcase);
CheckItemNo($itemno,$DTS);

my $baseprice=$DTS->{price}[$showcase];
my($guild,$guildrate,$guildmargin)=CheckGuild($DT,$DTS,$baseprice);
my $saleprice=$baseprice+($guild==1 ? -$guildmargin : $guildmargin);

if($itemno!= $DTS->{showcase}[$showcase]
|| $price != $saleprice
|| !$DTS->{item}[$itemno-1]
)
{
	OutError('���i�≿�i���ω������悤�ł�');
}

$num=$DTS->{item}[$itemno-1] if $DTS->{item}[$itemno-1]<$num;
$num=int($DT->{money}/$price) if ($DT->{money}<$num*$price && $price > 0);
$num=0 if $num<0;

OutError('��₩���ł����H') if !$num;

$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if !$id;
my $usetime=GetTimeDeal($baseprice*$num,$itemno,$num);
UseTime($usetime);
my($taxrate,$tax)=GetSaleTax($itemno,$num,$baseprice*$num,GetUserTaxRate($DTS,$DTTaxrate));

$DTS->{item}[$itemno-1]-=$num;
$DTS->{itemtoday}{$itemno}+=$num;
$DT->{item}[$itemno-1]+=$num;
$DTS->{money}+=$num*$baseprice-$tax;
$DTS->{trush}+=int($num*$baseprice/2);
$DT->{money}-=$num*$price;
$DT->{paytoday}+=$num*$price;
$DTS->{saletoday}+=$num*$baseprice;
$DTS->{taxtoday}+=$tax;

EditGuildMoney($DT->{guild} ,-$guildmargin*$num) if $guild==1;
EditGuildMoney($DTS->{guild}, $guildmargin*$num) if $guild==2;

#����؂ꎞ�̐l�CDOWN(����X��) �����M���h�̏ꍇ��SKIP
if($DTS->{item}[$itemno-1]==0 && $guild!=1 && $guild!=-1)
{
	my $rankdown+=($DTS->{rank}/100)**3/1000; #�l�C�ɉ����ă_�E��
	#$rankdown+=70*4/($nowranking+3); #�����L���O�ɉ����ă_�E��

	if($rankdown<1 && $rankdown>0)
		{$rankdown=1 if rand(1/$rankdown)<1;}
	$DTS->{rank}-=int($rankdown);
	$DTS->{rank}=0 if $DTS->{rank}<0;
}

$ret=$DTS->{shopname}."���".$ITEM[$itemno]->{name}."��".$num.$ITEM[$itemno]->{scale}.'@'.GetMoneyString($price)."(�v".GetMoneyString($price*$num).")";
$ret.=(($ITEM[$itemno]->{flag}=~/h/) ? "�ɂČق��܂���" : "�ɂĎd����܂���");
$ret.="/".GetTime2HMS($usetime)."����";
$ret.="/".('�M���h������','�M���h�Ԋ���')[$guild-1].'@'.GetMoneyString($guildmargin) if $guild>0;
$ret.="/�M���h�������⏕�Ȃ�" if $guild==-1;
PushLog(0,$DT->{id},$ret);

@item::DT=@DT;
$item::DT=$DT;
@item::ITEM=@ITEM;
$item::ITEM=$ITEM;
$item::BUY={
	dt		=>	$DT,
	dts		=>	$DTS,
	whole	=>	$DTS->{_wholestore_},
	item	=>	$ITEM[$itemno],
	itemno	=>	$itemno,
	num		=>	$num,
	price	=>	$price,
	baseprice=>	$baseprice,
	tax		=>	$tax,
	guild	=>	$guild,
	guildmargin	=>	$guildmargin,
};
RequireFile("inc-item.cgi");
require "$ITEM_DIR/funcbuy.cgi" if $DEFINE_FUNCBUY;

if($ITEM[$itemno]->{funcbuy})
{
	#@@item funcb ����
	my $item=$ITEM[$itemno];
	my $file="$ITEM_DIR/item-b/$item->{no}$FILE_EXT";
	my $func="item::".$item->{funcsale};
	my $funcexists=defined &$func;
	require $file if -e $file;
	&$func($item::BUY);
	undef &$func if !$funcexists;
	delete $INC{$file};
	undef @item::DT;
	undef $item::DT;
	undef @item::ITEM;
	undef $item::ITEM;
}

SetWholeStore($DTS) if $id==0;

WriteGuildData() if $guild>0;
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$TBT.$TRT.$TD.GetTagImgJob($DT->{job},$DT->{icon});
$disp.=$TD.GetMenuTag('stock',	'[�q�ɂ�]');
$disp.=($id==0) ? GetMenuTag('shop-m','[�d����𑱂���]') : GetMenuTag('shop-a','[�������𑱂���]','&t=2');
$disp.=$TRE.$TBE;
$disp.="<br>".$ret;

OutSkin();
1;

# �A�C�e���ڍו\�� 2005/01/06 �R��

$NOMENU=1;
Turn();
DataRead();
CheckUserPass();

$itemno=$Q{no};
$showcase=$Q{sc};
CheckItemNo($itemno);

RequireFile('inc-html-ownerinfo.cgi');

GetMarketStatus();

$disp.="<BIG>���q��</BIG><br><br>";

my $ITEM=$ITEM[$itemno];
$disp.= GetTagImgItemType($itemno,0,2).$ITEM->{name};
$disp.= GetTagImgItemType(0,$ITEM[$itemno]->{type})."<br><br>";

$disp.=$TB;
$disp.="$TR$TDB�݌�$TD$DT->{item}[$itemno-1] $ITEM->{scale}$TRE";
$disp.="$TR$TDB�W�����i$TD".GetMoneyString($ITEM->{price}).$TRE;
$disp.="$TR$TDB�ێ���$TD".GetMoneyString($ITEM->{cost}).$TRE;
$disp.="$TR$TDB����$TD$ITEM->{info}$TRE";

unless ($ITEM->{flag}=~/s/) {	# ��s��
	if($ITEM->{marketprice})
	{
	$disp.="$TR$TDB����$TD".GetMoneyString($ITEM->{marketprice}).$TRE;
	$disp.="$TR$TDB�ň��l$TD".GetMoneyString($ITEM->{marketpricelow}).$TRE;
	$disp.="$TR$TDB�ō��l$TD".GetMoneyString($ITEM->{marketpricehigh}).$TRE;
	}
	else
	{
	$disp.="$TR$TDB����$TD�̔��X�܂Ȃ�$TRE";
	}
	$disp.="$TR$TDB����$TD".GetMarketStatusGraph($ITEM->{uppoint})."$TRE";
}
$disp.=$TBE;

if($ITEM->{flag}=~/s/)
	{
	$disp.="<hr width=500 noshade size=1>";
	$disp.='��'.$ITEM[$itemno]->{name}.'��̔����邱�Ƃ͂ł��܂���<br>';
	}
	else
	{
	$disp.="�����̏��i�͒񂵂Ă�����܂���<br>" if ( $ITEM->{popular}==0);
	$disp.="�����̏��i�͒񂵂Ă��قƂ�ǔ���܂���<br>" if ( $ITEM->{popular} > 800000);
	$disp.="<hr width=500 noshade size=1>";
	RequireFile('inc-item-show.cgi');
	}

$disp.="<hr width=500 noshade size=1>";
if($ITEM->{flag}=~/t/)
	{
	$disp.='��'.$ITEM[$itemno]->{name}.'��'.(($ITEM->{flag}=~/h/)? "����" : "�j��").'���邱�Ƃ͂ł��܂���<br>';
	}
	else
	{
	RequireFile('inc-item-throw.cgi');
	}

$disp.="<hr width=500 noshade size=1>";
$itemcode=GetPath($ITEM_DIR,"use",$ITEM[$itemno]->{code});
if($itemcode ne '' && -e $itemcode)
{
	my $ITEM=$ITEM[$itemno];
	@item::DT=@DT;
	$item::DT=$DT;
	@item::ITEM=@ITEM;
	$item::ITEM=$ITEM;
	RequireFile('inc-item.cgi');
	require $itemcode;
	@USE=GetUseItemList();

	if($USE[0]->{name} ne '')
	{
	foreach my $USE (@USE)
		{
	$disp.="��";
	$disp.=qq|<a href="action.cgi?key=item-m&item=$itemno&no=$USE->{no}&$USERPASSURL&bk=$Q{bk}">| if $USE->{useok};
	$disp.=($USE->{useok} || $USE->{dispok}) ? $USE->{name} : "�H�H�H�H�H�H�H�H";
	$disp.="</a>" if $USE->{useok};
	$disp.="<br>";
		}
	}
}
OutSkin();
1;

use utf8;
# 陳列棚下請け 2005/01/06 由來

my $showcasecount=$DT->{showcasecount};

$disp.="<BIG>●" . l('陳列棚：現在%1個：維持費 %2',$showcasecount,GetMoneyString($SHOWCASE_COST[$showcasecount-1])) . "</BIG><br><br>";

my $usertaxrate=GetUserTaxRate($DT,$DTTaxrate);

$disp.=$TB;
if(!$MOBILE)
{
	my @taxmode=('',l('(免税)'),l('(倍税)'));
	$disp.=$TR;
	$disp.=$TDB.l('棚No.');
	$disp.=$TDB.l('商品名');
	$disp.=$TDB.l('売値');
	$disp.=$TDB.l('標準価格');
	$disp.=$TDB.l('売却税').$taxmode[$DT->{taxmode}+0];
	$disp.=$TDB.l('在庫数');
	$disp.=$TDB.l('今期売上数');
	$disp.=$TDB.l('前期売上数');
	$disp.=$TD;
	$disp.=$TRE;
}
else
{
	$tdh_pr{$MOBILE}=l('売値').':';
	$tdh_sp{$MOBILE}=l('標準').':';
	$tdh_tx{$MOBILE}=l('売税').':';
	$tdh_st{$MOBILE}=l('在庫').':';
	$tdh_ts{$MOBILE}=l('本売').':';
	$tdh_ys{$MOBILE}=l('昨売').':';
}

for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
{
	my $itemno=$DT->{showcase}[$cnt];
	my $ITEM=$ITEM[$itemno];
	my $scale=$ITEM->{scale};
	my $stock=$itemno ? $DT->{item}[$itemno-1]:0;

	$disp.=$TR.$TD."<SPAN>" . l('棚%1',$cnt+1)."</SPAN>";
	$disp.=$TD;
	$disp.="<A HREF=\"action.cgi?key=item&$USERPASSURL&no=$itemno&sc=".($cnt+1)."&pr=".$DT->{price}[$cnt]."&bk=$Q{key}\">" if $stock;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if $stock;
	
	if($itemno)
	{
		my($taxrate,$tax)=GetSaleTax($itemno,1,$DT->{price}[$cnt],$usertaxrate);
		$disp.=$TD.$tdh_pr{$MOBILE}.GetMoneyString($DT->{price}[$cnt]);
		$disp.=$TD.$tdh_sp{$MOBILE}.GetMoneyString($ITEM->{price});
		$disp.=$TD.$tdh_tx{$MOBILE}.GetMoneyString($tax).l(' (税率%1%)',$taxrate);
		$disp.=$TD.$tdh_st{$MOBILE}.$stock.$scale;
		$disp.=$TD.$tdh_ts{$MOBILE}.($DT->{itemtoday}{$itemno}+0).$scale;
		$disp.=$TD.$tdh_ys{$MOBILE}.($DT->{itemyesterday}{$itemno}+0).$scale;
		$disp.=$TD.'<A HREF="action.cgi?key=sc-s&'.$USERPASSURL.'&item=0&no='.$cnt.'&bk=sc">' . l('陳列中止') .'</A>';
	}
	else
	{
		$disp.=$TD.$TD.$TD.$TD.$TD.$TD;
	}
	$disp.=$TRE;
}
$disp.=$TBE;
1;

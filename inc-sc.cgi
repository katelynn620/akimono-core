# ��I������ 2005/01/06 �R��

my $showcasecount=$DT->{showcasecount};

$disp.="<BIG>����I�F����$showcasecount�F�ێ��� ".GetMoneyString($SHOWCASE_COST[$showcasecount-1])."</BIG><br><br>";

my $usertaxrate=GetUserTaxRate($DT,$DTTaxrate);

$disp.=$TB;
if(!$MOBILE)
{
	my @taxmode=('','(�Ɛ�)','(�{��)');
	$disp.=$TR;
	$disp.=$TDB."�INo.";
	$disp.=$TDB."���i��";
	$disp.=$TDB."���l";
	$disp.=$TDB."�W�����i";
	$disp.=$TDB."���p��".$taxmode[$DT->{taxmode}+0];
	$disp.=$TDB."�݌ɐ�";
	$disp.=$TDB."�������㐔";
	$disp.=$TDB."�O�����㐔";
	$disp.=$TD;
	$disp.=$TRE;
}
else
{
	$tdh_pr{$MOBILE}="���l:";
	$tdh_sp{$MOBILE}="�W��:";
	$tdh_tx{$MOBILE}="����:";
	$tdh_st{$MOBILE}="�݌�:";
	$tdh_ts{$MOBILE}="�{��:";
	$tdh_ys{$MOBILE}="��:";
}

for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
{
	my $itemno=$DT->{showcase}[$cnt];
	my $ITEM=$ITEM[$itemno];
	my $scale=$ITEM->{scale};
	my $stock=$itemno ? $DT->{item}[$itemno-1]:0;

	$disp.=$TR.$TD."<SPAN>�I".($cnt+1)."</SPAN>";
	$disp.=$TD;
	$disp.="<A HREF=\"action.cgi?key=item&$USERPASSURL&no=$itemno&sc=".($cnt+1)."&pr=".$DT->{price}[$cnt]."&bk=$Q{key}\">" if $stock;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if $stock;
	
	if($itemno)
	{
		my($taxrate,$tax)=GetSaleTax($itemno,1,$DT->{price}[$cnt],$usertaxrate);
		$disp.=$TD.$tdh_pr{$MOBILE}.GetMoneyString($DT->{price}[$cnt]);
		$disp.=$TD.$tdh_sp{$MOBILE}.GetMoneyString($ITEM->{price});
		$disp.=$TD.$tdh_tx{$MOBILE}.GetMoneyString($tax)." (�ŗ�".$taxrate."%)";
		$disp.=$TD.$tdh_st{$MOBILE}.$stock.$scale;
		$disp.=$TD.$tdh_ts{$MOBILE}.($DT->{itemtoday}{$itemno}+0).$scale;
		$disp.=$TD.$tdh_ys{$MOBILE}.($DT->{itemyesterday}{$itemno}+0).$scale;
		$disp.=$TD.'<A HREF="action.cgi?key=sc-s&'.$USERPASSURL.'&item=0&no='.$cnt.'&bk=sc">�񒆎~</A>';
	}
	else
	{
		$disp.=$TD.$TD.$TD.$TD.$TD.$TD;
	}
	$disp.=$TRE;
}
$disp.=$TBE;
1;

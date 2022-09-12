use utf8;
# 倉庫 2005/01/06 由來

DataRead();
CheckUserPass();

$MENUSAY=GetMenuTag('log',l('[新聞]'))
	.GetMenuTag('shop-a',	l('[商店通りへ]'))
	.GetMenuTag('shop-m',	l('[市場へ]'))
	.GetMenuTag('main',	l('[店内に戻る]'));

RequireFile('inc-html-ownerinfo.cgi');

if ($DT->{trush} > 5000000)
	{
	$disp.="<BIG>●".l('倉庫')."</BIG><br><br>";
	$disp.=$TB.$TR.$TD.GetTagImgKao(l('お手伝い'),"help").$TD;
	$disp.="<SPAN>".l('お手伝い')."</SPAN>：".l('商品がごみの中にうずもれていて，見つけられません。');
	$disp.="<br>".l('先にお掃除して，ごみを片付けましょう。').$TRE.$TBE;
	$disp.="<br>".GetMenuTag('sweep',l('[お掃除へ]'));
	OutSkin();
	exit;
	}

my $tp=$Q{tp};
my $pg=$Q{pg};

my $DTitem=$DT->{item};
my $DTitemtoday=$DT->{itemtoday};
my $DTitemyesterday=$DT->{itemyesterday};
my $DTexp=$DT->{exp};

foreach my $no(1..$MAX_ITEM)
{
	$ITEM=$ITEM[$no];
	next if (!$DTitem->[$no-1] && !$DTitemtoday->{$no} && !$DTexp->{$no});
	if ($ITEM->{flag}=~/s/)	# s 陳列不可
	{
	$itema{$no}=$ITEM;
	}
	else
	{
	next if ($ITEM->{type} != $tp)&&($tp != 0);;
	$itemb{$no}=$ITEM;
	}
}

GetMarketStatus();

my %showcase=();
my $itemno;
foreach(0..$DT->{showcasecount}-1)
{
	next if !($itemno=$DT->{showcase}[$_]);
	$showcase{$itemno}.=l('棚').($_+1).GetMoneyString($DT->{price}[$_])." ";
}

if(%itema)
{
	$disp.="<BIG>●".l('保管倉庫')."</BIG><br><br>";
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp=l('標準').':';
		$tdh_cs=l('維持').':';
		$tdh_st=l('在庫').':';
		$tdh_ex=l('熟練').':';
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				(
					l('名称'),
					l('標準価格'),
					l('維持費'),
					l('数量').'<small>/'.l('最大').'</small>',
					l('熟練'),
				)
			).$TRE;
	}
	
	foreach my $ITEM (sort{$a->{sort} <=> $b->{sort}} values(%itema))
	{
		my $cnt=$ITEM->{no};
		my $name=GetTagImgItemType($cnt).$ITEM->{name};
		$name="<A HREF=\"action.cgi?key=item&no=$cnt&bk=s&$USERPASSURL\">".$name."</A>" if $DTitem->[$cnt-1];
		
		$disp.=$TR.$TD.
			join($TD,
				$name,
				$tdh_sp.GetMoneyString($ITEM->{price}),
				$tdh_cs.GetMoneyString($ITEM->{cost}),
				$tdh_st.$DTitem->[$cnt-1]."<small>/".$ITEM->{limit}."</small>",
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '　'),
			);
	}
	$disp.=$TBE."<hr width=500 noshade size=1>";
}

$disp.="<BIG>●".l('販売倉庫')."</BIG><br><br>";
foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=stock&$USERPASSURL&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}

if(!%itemb)
{
	$disp.="<hr width=500 noshade size=1>".l('在庫がありません');
}
else
{
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp=l('標準').':';
		$tdh_cs=l('維持').':';
		$tdh_ts=l('本昨売').':';
		$tdh_ex=l('熟練').':';
		$tdh_sc=l('陳列').':';
		$tdh_mp=l('相場').':';
		$tdh_mb=l('需給').':';
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				(
					l('名称'),
					l('標準価格'),
					l('維持費'),
					l('数量<small>/最大</small>'),
					l('売上数<small>/前期</small>'),
					l('熟練'),
					l('陳列'),
					l('販売相場'),
					l('需要供給バランス'),
				)
			).$TRE;
	}
	
	foreach my $ITEM (sort{$a->{sort} <=> $b->{sort}} values(%itemb))
	{
		my $cnt=$ITEM->{no};
		my $name=GetTagImgItemType($cnt).$ITEM->{name};
		$name="<A HREF=\"action.cgi?key=item&no=$cnt&bk=s&$USERPASSURL\">".$name."</A>" if $DTitem->[$cnt-1];
		
		$disp.=$TR.$TD.
			join($TD,
				$name,
				$tdh_sp.GetMoneyString($ITEM->{price}),
				$tdh_cs.GetMoneyString($ITEM->{cost}),
				$tdh_st.$DTitem->[$cnt-1]."<small>/".$ITEM->{limit}."</small>",
				$tdh_ts.($DTitemtoday->{$cnt} || $DTitemyesterday->{$cnt} ? ($DTitemtoday->{$cnt}||0)."<small>/".($DTitemyesterday->{$cnt}||0)."</small>" : '　'),
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '　'),
				$tdh_sc.($showcase{$cnt}||'　'),
				$tdh_mp.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketprice}) : '　'),
			);
		$disp.=$TDNW.$tdh_mb.GetMarketStatusGraph($ITEM->{uppoint}||=10).$TRE;
	}
	$disp.=$TBE;
}
OutSkin();
1;

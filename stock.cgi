# �q�� 2005/01/06 �R��

DataRead();
CheckUserPass();

$MENUSAY=GetMenuTag('log','[�V��]')
	.GetMenuTag('shop-a',	'[���X�ʂ��]')
	.GetMenuTag('shop-m',	'[�s���]')
	.GetMenuTag('main',	'[�X���ɖ߂�]');

RequireFile('inc-html-ownerinfo.cgi');

if ($DT->{trush} > 5000000)
	{
	$disp.="<BIG>���q��</BIG><br><br>";
	$disp.=$TB.$TR.$TD.GetTagImgKao("����`��","help").$TD;
	$disp.="<SPAN>����`��</SPAN>�F���i�����݂̒��ɂ�������Ă��āC�������܂���B";
	$disp.="<br>��ɂ��|�����āC���݂�Еt���܂��傤�B".$TRE.$TBE;
	$disp.="<br>".GetMenuTag('sweep','[���|����]');
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
	if ($ITEM->{flag}=~/s/)	# s ��s��
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
	$showcase{$itemno}.="�I".($_+1).GetMoneyString($DT->{price}[$_])." ";
}

if(%itema)
{
	$disp.="<BIG>���ۊǑq��</BIG><br><br>";
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp="�W��:";
		$tdh_cs="�ێ�:";
		$tdh_st="�݌�:";
		$tdh_ex="�n��:";
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				qw(
					����
					�W�����i
					�ێ���
					����<small>/�ő�</small>
					�n��
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
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '�@'),
			);
	}
	$disp.=$TBE."<hr width=500 noshade size=1>";
}

$disp.="<BIG>���̔��q��</BIG><br><br>";
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
	$disp.="<hr width=500 noshade size=1>�݌ɂ�����܂���";
}
else
{
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp="�W��:";
		$tdh_cs="�ێ�:";
		$tdh_ts="�{��:";
		$tdh_ex="�n��:";
		$tdh_sc="��:";
		$tdh_mp="����:";
		$tdh_mb="����:";
	}
	else
	{
		$disp.=$TR.$TDB.
			join($TDB,
				qw(
					����
					�W�����i
					�ێ���
					����<small>/�ő�</small>
					���㐔<small>/�O��</small>
					�n��
					��
					�̔�����
					���v�����o�����X
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
				$tdh_ts.($DTitemtoday->{$cnt} || $DTitemyesterday->{$cnt} ? ($DTitemtoday->{$cnt}||0)."<small>/".($DTitemyesterday->{$cnt}||0)."</small>" : '�@'),
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '�@'),
				$tdh_sc.($showcase{$cnt}||'�@'),
				$tdh_mp.($ITEM->{marketprice} ? GetMoneyString($ITEM->{marketprice}) : '�@'),
			);
		$disp.=$TDNW.$tdh_mb.GetMarketStatusGraph($ITEM->{uppoint}||=10).$TRE;
	}
	$disp.=$TBE;
}
OutSkin();
1;

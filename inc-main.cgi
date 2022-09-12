use utf8;
# 店内表示 2005/01/06 由來

ReadLetter();

# 画像定義
my $space='<IMG class="i" SRC="'.$IMAGE_URL.'/map/dummy.png">';
my $vspace='<IMG WIDTH="64" HEIGHT="16" SRC="'.$IMAGE_URL.'/map/dummy.png">';
$gold='<IMG width="24" height="24" SRC="'.$IMAGE_URL.'/map/c-sg.png">';
$trush='<IMG class="c" SRC="'.$IMAGE_URL.'/map/c-st.png">';
my $post=GetMenuTag('letter','<acronym title="'.l('郵便箱').'"><IMG class="c" SRC="'.$IMAGE_URL.'/map/c-sp.png"></acronym>');
my $news=GetMenuTag('log','<acronym title="'.l('新聞').'"><IMG width="24" height="26" SRC="'.$IMAGE_URL.'/map/c-sn.png"></acronym>');
my $stock=GetMenuTag('stock','<acronym title="'.l('倉庫').'"><IMG WIDTH="90" HEIGHT="42" SRC="'.$IMAGE_URL.'/map/shops.png"></acronym>');
my $dwarf=GetMenuTag('dwarf','<acronym title="'.l('ドワーフ宅配便').'"><IMG class="c" SRC="'.$IMAGE_URL.'/map/c-s11.png"></acronym>');

$image[0]='<td WIDTH="208" HEIGHT="64" style="background-image : url('.$IMAGE_URL.'/map/shop1a.png)">';
$image[1]='<td valign=bottom WIDTH="96" style="background-image : url('.$IMAGE_URL.'/map/shop2a.png)">';
$image[2]='<td HEIGHT="80" align=center valign=top style="background-image : url('.$IMAGE_URL.'/map/shop1b.png)">';
$image[3]='<td style="background-image : url('.$IMAGE_URL.'/map/shop2b.png)">';
$image[4]='<td HEIGHT="48" align=center valign=top style="background-image : url('.$IMAGE_URL.'/map/shop1c.png)">';
$image[5]='<td valign=top style="background-image : url('.$IMAGE_URL.'/map/shop2c.png)">';

$disp.="<BIG>●".$DT->{shopname}.l("店内")."</BIG><br><br>";

DevelopImage();
HelpMessage();

CharaDefine();
StyleDefine();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE=user>
<INPUT TYPE=HIDDEN NAME=mode VALUE=comment>
$USERPASSFORM
<table class=t cellpadding=0 cellspacing=0>
$TRT$image[0]$image[1]$dwarf
<td rowspan=3 valign=bottom>
$post
<td rowspan=3>
HTML

OwnerInfo();

$disp.=<<"HTML";
$TRE
$TRT$image[2]$news$gold<br>$helper<br>$show$image[3]$trush
$TRE
$TRT$image[4]$chara$image[5]$stock
$TRE$TBE
</FORM>
HTML

1;


sub OwnerInfo
{
	my $tm=$NOW_TIME-$DT->{time};
	if($tm<0)
	{
		$tm=-$tm;
		$tm=l('行動可能まであと %1',GetTime2HMS($tm));
	}
	else
	{
		$tm=$MAX_STOCK_TIME if $tm>$MAX_STOCK_TIME;
		$tm=GetTime2HMS($tm);
	}
	my $moneymsg=GetMoneyString($DT->{money});
	my $rankmsg=GetRankMessage($DT->{rank});
	my $cleanmsg=GetCleanMessage($DT->{trush});

	$disp.=<<STR;
	<table align=center>$TR<td width=48>
STR
	$disp.=GetTagImgKao($DT->{name},$DT->{icon})."<br>";
	$disp.=$TD."<SPAN>RANK</SPAN> ".($id2idx{$DT->{id}}+1).GetTopCountImage($DT->{rankingcount}).DignityDefine($DT->{dignity},1)."<br>";
	$disp.=GetTagImgGuild($DT->{guild})."<b>".$DT->{shopname}."</b>".$TRE;

	# I18N
	my $timestr = l('時間#A');
	$timestr =~ s/#A//g;

	$disp.= "$TR$TDB" . l("資金") . "$TD$moneymsg$TRE
	$TR$TDB$timestr$TD$tm$TRE
	$TR$TDB" . l("人気") . "$TD$rankmsg$TRE
	$TR$TDB" . l("ごみ") . "$TD$cleanmsg$TRE
	$TR$TDB" . l("コメント") . "$TD<INPUT TYPE=TEXT NAME=cmt SIZE=20 VALUE=\"$DT->{comment}\">
	<INPUT TYPE=SUBMIT VALUE=\"".l('変更')."\">$TRE$TBE";
}


sub StyleDefine
{
	my $ii=<<'HTML';
<Style Type="text/css">
<!--
HTML
	my $i=<<"HTML";
<Style Type="text/css">
<!--
acronym  { border-style:none;}
HTML
	$DISP{TOP} =~ s/$ii/$i/;
}

sub CharaDefine
{
$chara="";
my $i=int($NOW_TIME / 3600) % 3;
if (!$show)
	{
	$helper=TagChara(l('在庫を切らしちゃってるんです。スミマセン…'),"0");
	if ($i == 0)
		{
		$chara=TagChara(l('ありゃりゃ，何にも売ってないぞ。困った。'),"1").$vspace;
		}
	elsif ($i == 1)
		{
		$chara=$vspace.TagChara(l('せっかく買いに来たのに何にもない…。どうしよう？'),"2").TagChara(l('しょうがないね。もうちょっと待ってみる？'),"3");
		}
	else
		{
		$chara=TagChara(l('ねぇねぇお姉ちゃん，なんでここには何にもないの？'),"4");
		}
	}
else
	{
	$helper=TagChara(l('いらっしゃいませっ'),"0");
	if ($i == 0)
		{
		$chara=$vspace.TagChara(l('どれどれ。今日の買いどころは…'),"5");
		}
	elsif ($i == 1)
		{
		$chara=TagChara(l('ん～，これくださいな。'),"6").$vspace;
		}
	elsif ($DT->{rank} < 5500)
		{
		$chara=TagChara(l('うーん，そこそこ良い店ではあるんだけどね…'),"7").TagChara(l('もう一声っていう感じなのよねぇ…'),"8").$vspace;
		}
	else
		{
		$chara=$vspace.TagChara(l('ここはなかなか良いところだな。'),"9").TagChara(l('そうじゃな。わしもよく寄る店じゃ。'),"10");
		}
	}
}

sub TagChara
{
	my($ii,$i)=@_;
	return qq|<acronym title="$ii"><IMG class="c" SRC="$IMAGE_URL/map/c-s$i.png"></acronym>|;
}

sub HelpMessage
{
$disp.=$TB.$TR.$TD.GetTagImgKao(l('お手伝い'),"help").$TD;

	if ($NeverR)
	{
		$disp.='
			<SPAN>'.l('お手伝い').'</SPAN>：'.l('新しい手紙が %1通届いております。',$NeverR).'<br>'
			.l('郵便箱を開けてみてください。');
	}
	elsif ( ($NOW_TIME-$DT->{foundation}) < 3600*3 )
	{
		$disp.='
			<SPAN>'.l('お手伝い').'</SPAN>：'.l('はじめまして。私が店のお手伝いをさせてもらってます。').'<br>'
			.l('さっそくですが店長さま，')
			.l('<A HREF="action.cgi?key=library&t=1" TARGET=_blank>[ゲームのやり方]</A>はご存知ですか？');
		}
	elsif ($DT->{trush} > 4000000)
	{
		$disp.='
			<SPAN>'.l('お手伝い').'</SPAN>：'.l('店長さま，お帰りなさいませ。').'<br>'
			.l('お店の中が汚れてきています。そろそろ掃除したらいかがでしょう。');
	}
	elsif (!$show)
	{
		$disp.='
			<SPAN>'.l('お手伝い').'</SPAN>：'.l('店長さま，売る物がなくなってしまいました。').'<br>'
			.l('すぐに在庫を補充するか，代わりのものを売りに出しましょう。');
	}
	else
	{
		$disp.='
			<SPAN>'.l('お手伝い').'</SPAN>：'.l('店長さま，お帰りなさいませ。').'<br>'
			.l('お店はいまのところ順調ですよ。');
	}
$disp.=$TRE.$TBE."<br>";
}

sub DevelopImage
{
my $i=int($DT->{money} / 5000000);
if ($i < 1)
	{
	$gold=""
	}
	else
	{
	$i=6 if $i > 6;
	$gold x= $i;
	}
$i=int(0.9 + $DT->{trush} / 1000000);
if ($i < 1)
	{
	$trush=""
	}
	elsif ($i > 3)
	{
	$i -=3;
	$i=3 if $i > 3;
	$trush = ($trush x $i)."<br>".($trush x 3);
	}
	else
	{
	$trush x= $i;
	}
$trush=GetMenuTag('sweep','<acronym title="ごみ袋">'.$trush.'<acronym>') if $trush;
$show="";
for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
{
	my $itemno=$DT->{showcase}[$cnt];
	my $ITEM=$ITEM[$itemno];
	my $stock=$itemno ? $DT->{item}[$itemno-1]:0;
	next if !$stock;
	$show.=GetTagImgItemType($itemno)
}
}

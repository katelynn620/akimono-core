# �X���\�� 2005/01/06 �R��

ReadLetter();

# �摜��`
my $space='<IMG class="i" SRC="'.$IMAGE_URL.'/map/dummy.png">';
my $vspace='<IMG WIDTH="64" HEIGHT="16" SRC="'.$IMAGE_URL.'/map/dummy.png">';
$gold='<IMG width="24" height="24" SRC="'.$IMAGE_URL.'/map/c-sg.png">';
$trush='<IMG class="c" SRC="'.$IMAGE_URL.'/map/c-st.png">';
my $post=GetMenuTag('letter','<acronym title="�X�֔�"><IMG class="c" SRC="'.$IMAGE_URL.'/map/c-sp.png"></acronym>');
my $news=GetMenuTag('log','<acronym title="�V��"><IMG width="24" height="26" SRC="'.$IMAGE_URL.'/map/c-sn.png"></acronym>');
my $stock=GetMenuTag('stock','<acronym title="�q��"><IMG WIDTH="90" HEIGHT="42" SRC="'.$IMAGE_URL.'/map/shops.png"></acronym>');
my $dwarf=GetMenuTag('dwarf','<acronym title="�h���[�t��z��"><IMG class="c" SRC="'.$IMAGE_URL.'/map/c-s11.png"></acronym>');

$image[0]='<td WIDTH="208" HEIGHT="64" style="background-image : url('.$IMAGE_URL.'/map/shop1a.png)">';
$image[1]='<td valign=bottom WIDTH="96" style="background-image : url('.$IMAGE_URL.'/map/shop2a.png)">';
$image[2]='<td HEIGHT="80" align=center valign=top style="background-image : url('.$IMAGE_URL.'/map/shop1b.png)">';
$image[3]='<td style="background-image : url('.$IMAGE_URL.'/map/shop2b.png)">';
$image[4]='<td HEIGHT="48" align=center valign=top style="background-image : url('.$IMAGE_URL.'/map/shop1c.png)">';
$image[5]='<td valign=top style="background-image : url('.$IMAGE_URL.'/map/shop2c.png)">';

$disp.="<BIG>��".$DT->{shopname}."�X��</BIG><br><br>";

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
		$tm='�s���\�܂ł��� '.GetTime2HMS($tm);
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
	$disp.=<<STR;
	$TR$TDB����$TD$moneymsg$TRE
	$TR$TDB����$TD$tm$TRE
	$TR$TDB�l�C$TD$rankmsg$TRE
	$TR$TDB����$TD$cleanmsg$TRE
	$TR$TDB�R�����g$TD<INPUT TYPE=TEXT NAME=cmt SIZE=20 VALUE="$DT->{comment}">
	<INPUT TYPE=SUBMIT VALUE="�ύX">$TRE$TBE
STR
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
	$helper=TagChara("�݌ɂ�؂炵������Ă��ł��B�X�~�}�Z���c","0");
	if ($i == 0)
		{
		$chara=TagChara("�������C���ɂ������ĂȂ����B�������B","1").$vspace;
		}
	elsif ($i == 1)
		{
		$chara=$vspace.TagChara("�������������ɗ����̂ɉ��ɂ��Ȃ��c�B�ǂ����悤�H","2").TagChara("���傤���Ȃ��ˁB����������Ƒ҂��Ă݂�H","3");
		}
	else
		{
		$chara=TagChara("�˂��˂����o�����C�Ȃ�ł����ɂ͉��ɂ��Ȃ��́H","4");
		}
	}
else
	{
	$helper=TagChara("��������Ⴂ�܂���","0");
	if ($i == 0)
		{
		$chara=$vspace.TagChara("�ǂ�ǂ�B�����̔����ǂ���́c","5");
		}
	elsif ($i == 1)
		{
		$chara=TagChara("��`�C���ꂭ�������ȁB","6").$vspace;
		}
	elsif ($DT->{rank} < 5500)
		{
		$chara=TagChara("���[��C���������ǂ��X�ł͂���񂾂��ǂˁc","7").TagChara("�����ꐺ���Ă��������Ȃ̂�˂��c","8").$vspace;
		}
	else
		{
		$chara=$vspace.TagChara("�����͂Ȃ��Ȃ��ǂ��Ƃ��낾�ȁB","9").TagChara("��������ȁB�킵���悭���X����B","10");
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
$disp.=$TB.$TR.$TD.GetTagImgKao("����`��","help").$TD;

 if ($NeverR)
	{
$disp.=<<"HTML";
	<SPAN>����`��</SPAN>�F�V�����莆�� $NeverR�ʓ͂��Ă���܂��B<br>
	�X�֔����J���Ă݂Ă��������B
HTML
	}
	elsif ( ($NOW_TIME-$DT->{foundation}) < 3600*3 )
	{
$disp.=<<'HTML';
	<SPAN>����`��</SPAN>�F�͂��߂܂��āB�����X�̂���`���������Ă�����Ă܂��B<br>
	���������ł����X�����܁C<A HREF="action.cgi?key=library&t=1" TARGET=_blank>
	[�Q�[���̂���]</A>�͂����m�ł����H
HTML
	}
	elsif ($DT->{trush} > 4000000)
	{
$disp.=<<'HTML';
	<SPAN>����`��</SPAN>�F�X�����܁C���A��Ȃ����܂��B<br>
	���X�̒�������Ă��Ă��܂��B���낻��|�������炢�����ł��傤�B
HTML
	}
	elsif (!$show)
	{
$disp.=<<'HTML';
	<SPAN>����`��</SPAN>�F�X�����܁C���镨���Ȃ��Ȃ��Ă��܂��܂����B<br>
	�����ɍ݌ɂ��[���邩�C����̂��̂𔄂�ɏo���܂��傤�B
HTML
	}
	else
	{
$disp.=<<'HTML';
	<SPAN>����`��</SPAN>�F�X�����܁C���A��Ȃ����܂��B<br>
	���X�͂��܂̂Ƃ��돇���ł���B
HTML
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
$trush=GetMenuTag('sweep','<acronym title="���ݑ�">'.$trush.'<acronym>') if $trush;
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

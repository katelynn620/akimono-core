use utf8;
# 宮殿 2004/01/20 由來

RequireFile("inc-palace.cgi");	#設定ファイル読み込み

$image[0]=GetTagImgKao(l("王様"),"king",'align="left" ');
$image[1]=GetTagImgKao(l("大臣"),"minister",'align="left" ');

DataRead();
CheckUserPass();

$evt=GetTownData('evt');
$evt=0 if (!$evt);
$level=DignityDefine($DT->{dignity});

$disp.="<BIG>●".l('宮殿')."</BIG><br><br>";

$shopname=$DT->{shopname};
$name=$DT->{name};
$need=$itemno[$evt];

if ($DT->{point} <  $deny_point )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[1].l('おや宮殿に御用ですか？<b>%1</b>の<b>%2</b>さん。',$shopname,$name).'<br>';
	$disp.=l('しかし国王陛下は%1さんとは面会できないとの仰せでございます。',$name);
	$disp.='<br>'.l('もう少し経営の手腕を高めてから来てみてはどうでしょう。').$TRE;
	$disp.=$TBE."<br>";
	}
	else
	{
	KingMain();
	}

OutSkin();
1;


sub KingMain
{
$disp.='<TABLE cellpadding="26" width="570"><tr>';
$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
$disp.=$image[0].l('よくぞ参った<b>%1</b>の<b>%2%3</b>よ。',$shopname,$name,$level).'<br>';
$disp.=l('活躍はかねがね聞き及んでおるぞ。そこでじゃ，そなたを見込んで使命を与える。').'<br><br>';
$disp.=$msg[$evt].'<br>'.l('されば<b>%1%2を%3%4</b>求めて参れ。',GetTagImgItemType($need),$ITEM[$need]->{name},$count[$evt],$ITEM[$need]->{scale});
$disp.='<br>'.l('この使命を見事果たせたならばそなたに%1<b>爵位経験値</b>を与える。やってくれるな？',DignityDefine(1,1)).$TRE;
$disp.=$TBE;

$disp.=<<"HTML";
<br><FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="palace-s">
$USERPASSFORM
<BIG>●${\l('使命達成')}</BIG>： ${\l('王様が依頼する商品を')}
<INPUT TYPE=SUBMIT VALUE="${\l('渡す')}"></FORM>
HTML
}
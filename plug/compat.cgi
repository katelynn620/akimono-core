use utf8;
# compat プラグイン 2004/01/20 由來

sub Compat
{
	OutError(l('互換性のないプログラムのため，実行することができません'));
}

sub OutHTML
{
	Compat();
}

1;

# Set proper $TERM if we are running gnome-terminal
if [ "$COLORTERM" == "gnome-terminal" ]
then
    TERM=xterm-256color
fi

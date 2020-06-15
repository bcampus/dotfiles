from typing import List  # noqa: F401

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.command import lazy

mod = "mod4"
terminal = "termite"
defaultWebBrowser = "qutebrowser"
defaultFileManager = "pcmanfm"
defaultEmailClient = "evolution"

keys = [
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(),
        desc='Move focus to prev monitor'),

    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Shrink and grow layout
    Key([mod], "h", lazy.layout.grow(), lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod], "l", lazy.layout.shrink(), lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating on active screen"),

    # multiple stack panes
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod, "shift"], "Return", lazy.spawn("rofi -show run"), desc="Show rofi run"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Rofi scripts
    Key([mod, "mod1"], "w", lazy.spawn("rofiweb"), desc="Run rofi web script"),

    # *** PROGRAM SHORTCUTS ***
    Key([mod, "control"], "w", lazy.spawn(defaultWebBrowser), desc="Start web browser"),
    Key([mod, "shift", "control"], "w", lazy.spawn("google-chrome"), desc="Start chrome"),
    Key([mod, "control"], "f", lazy.spawn(terminal + " -e 'vifm /home/ben'"), desc="vifm"),
    Key([mod, "shift", "control"], "f", lazy.spawn(defaultFileManager), desc="File manager"),
    Key([mod, "control"], "e", lazy.spawn(defaultEmailClient), desc="Start email client"),
    Key([mod, "control"], "h", lazy.spawn(terminal + " -e htop"), desc="Start htop"),
    Key([mod, "control"], "r", lazy.spawn(terminal + " -e tuir"), desc="Start reddit"),
]

groupNames = [("DEV", "1"),
              ("WB1", "2"),
              ("WB2", "3"),
              ("DOC", "4"),
              ("RND", "5"),
              ("MSC", "6"),
              ]

groups = [Group(name) for name, key in groupNames]

for name, key in groupNames:
    keys.extend([
        # mod + letter of group = switch to group
        Key([mod], key, lazy.group[name].toscreen(),
            desc="Switch to group {}".format(name)),

        # # mod + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #     desc="Switch to & move focused window to group {}".format(i.name)),
        # # Or, use below if you prefer not to switch to that group.
        # mod + shift + letter of group = move focused window to group
        Key([mod, "shift"], key, lazy.window.togroup(name), lazy.group[name].toscreen(),
            desc="move focused window to group {}".format(name)),
        Key([mod, "control"], key, lazy.window.togroup(name),
            desc="move focused window to group {}".format(name)),
    ])

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": "FF79C6",
                "border_normal": "1D2330"
                }

# COLORS
foregrounds = [
    ["#ffffff", "#ffffff"],  # 00 font color for group names
    ["#FF79C6", "#FF79C6"],  # 01 window name
    ["#ffffff", "#ffffff"],  # 02 Current Layout Text Colour
    ["#FF79C6", "#FF79C6"],  # 03 Time Colour
    ["#FF5555", "#FF5555"],  # 04 Volume Colour
    ["#F1FA8C", "#F1FA8C"],  # 05 CPU_Temp Colour
    ["#50FA7A", "#50FA7A"],  # 06 Updates Colour
]

backgrounds = [
    ["#282A36", "#282A36"],  # 00 panel background
    ["#373A4B", "#373A4B"],  # 01 background for current screen tab
    ["#373A4B", "#373A4B"],  # 02 Current layout background
    ["#2A101F", "#2A101F"],  # 03 Time Colour
    ["#2E1818", "#2E1818"],  # 04 Volume Colour
    ["#3E4029", "#3E4029"],  # 05 CPU_Temp Colour
    ["#233127", "#233127"],  # 06 Updates
]

borders = [
    ["#FF79C6", "#FF79C6"],  # 00 border line color for current tab
    ["#4E5266", "#4E5266"],  # 01 border line color for other tab
]

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(**layout_theme, num_stacks=2),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.Matrix(**layout_theme),

    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme, columnwidth=300),
]

# DEFAULT WIDGET SETTINGS
widget_defaults = dict(
    font="Monospace",
    fontsize=12,
    padding=2,
    background=backgrounds[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    padding=4,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.CurrentLayout(
                    padding=4,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.Sep(
                    padding=8,
                    linewidth=0,
                ),
                widget.GroupBox(
                    font="Ubuntu",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=3,
                    active=foregrounds[2],
                    inactive=foregrounds[2],
                    rounded=False,
                    highlight_color=backgrounds[1],
                    highlight_method="line",
                    this_current_screen_border=borders[0],
                    this_screen_border=borders[1],
                    other_current_screen_border=backgrounds[0],
                    other_screen_border=backgrounds[0],
                    foreground=foregrounds[2],
                    background=backgrounds[0]
                ),
                widget.WindowName(
                    padding=800,
                    foreground=foregrounds[1],
                ),
                widget.CheckUpdates(
                    display_format="🠕 {updates}",
                    distro="Fedora",
                    update_interval=30,
                    padding=10,
                    foreground=foregrounds[6],
                    colour_have_updates=foregrounds[6],
                    colour_no_updates=foregrounds[6],
                    background=backgrounds[6],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=3,
                    background=backgrounds[5],
                ),
                widget.TextBox(
                    text="💻",
                    background=backgrounds[5],
                    foreground=foregrounds[5],
                    padding=3,
                ),
                widget.ThermalSensor(
                    background=backgrounds[5],
                    foreground=foregrounds[5],
                    padding=6,
                    tag_sensor="Package id 0"
                ),
                widget.TextBox(
                    text="🕩",
                    background=backgrounds[4],
                    foreground=foregrounds[4],
                    padding=6
                ),
                widget.Volume(
                    background=backgrounds[4],
                    foreground=foregrounds[4],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=backgrounds[4],
                    foreground=foregrounds[4],
                ),
                widget.Clock(
                    format='%a %d %b %Y  %I:%M:%S %p',
                    padding=16,
                    background=backgrounds[3],
                    foreground=foregrounds[3],
                ),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    padding=4,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.CurrentLayout(
                    padding=4,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    foreground=foregrounds[2],
                    background=backgrounds[2],
                ),
                widget.Sep(
                    padding=8,
                    linewidth=0,
                ),
                widget.GroupBox(
                    font="Ubuntu",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=5,
                    borderwidth=3,
                    active=foregrounds[2],
                    inactive=foregrounds[2],
                    rounded=False,
                    highlight_color=backgrounds[1],
                    highlight_method="line",
                    this_current_screen_border=borders[0],
                    this_screen_border=borders[1],
                    other_current_screen_border=backgrounds[0],
                    other_screen_border=backgrounds[0],
                    foreground=foregrounds[2],
                    background=backgrounds[0]
                ),
                widget.WindowName(
                    padding=800,
                    foreground=foregrounds[1],
                ),
                widget.Clock(
                    format='%a %d %b %Y  %I:%M:%S %p',
                    padding=16,
                    background=backgrounds[3],
                    foreground=foregrounds[3],
                ),
            ],
            24,
        )
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

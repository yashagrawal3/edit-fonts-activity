from gi.repository import Gtk
# from gi.repository import Gdk
# import cairo
# import math
# from defcon import Font

from sugar3.graphics.icon import Icon
from sugar3.graphics import style
from editfonts.widgets.glyph_box import GlyphBox
import editfonts.globals as globals


class EditorPage(Gtk.Box):
    """
    This Class Creates the "Let's Edit Font:<familyName>" Page that loads up
    on clicking any Glyph in the Character Map or when the edit font button is
    clicked on the Font Summary page
    """

    def __init__(self):
        super(EditorPage, self).__init__()
        self._init_ui()

    def update(self, activity):
        self.activity = activity
        self.font = activity.main_font
        self.glyphName = activity.glyphName

    def _init_ui(self):

        self.set_property("orientation", Gtk.Orientation.HORIZONTAL)

        # create Right Toolbar
        """
        self.side_toolbar_right = self._create_right_toolbar()
        self.side_toolbar_right.set_property("border-width", 40)
        self.pack_end(self.side_toolbar_right, False, False, 10)
        """

        # create Left Toolbar

        self.side_toolbar_left = self._create_left_toolbar()
        self.side_toolbar_left.set_property("border-width", 40)
        self.pack_start(self.side_toolbar_left, False, False, 10)

        # Create Central Area
        self.vbox = Gtk.VBox()
        self.pack_start(self.vbox, True, True, 10)

        """
        self.heading = PageHeading("Let's Edit Font:" +
                                   globals.FONT.info.familyName,
                                   fontSize='20000')

        self.vbox.pack_start(self.heading, False, False, 30)
        self.vbox.pack_start(Gtk.HSeparator(),
                             False, False, 0)

        self.characterMap = CharacterMap(10, 1, 'BUTTON')
        self.vbox.pack_start(self.characterMap, False, False, 30)
        self.vbox.pack_start(Gtk.HSeparator(),
                             False, False, 0)

        """

        # Create Drawing Area

        self.editor_alignment = Gtk.Alignment(xalign=0.5,
                                              yalign=0.5,
                                              xscale=0,
                                              yscale=0)

        self.editor_area = GlyphBox()
        self.editor_alignment.add(self.editor_area)

        self.vbox.pack_start(self.editor_alignment, True, True, 0)

        # Add the Drawing Area inside a scrolling window
        """
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC,
                                   Gtk.PolicyType.AUTOMATIC)
        scrolled_window.set_border_width(10)
        scrolled_window.add_with_viewport(self.editor_alignment)

        self.vbox.pack_start(scrolled_window, True, True, 0)
        """

        self.show_all()

    def _create_right_toolbar(self):
        """
        This is a vertical toolbar for this page
        Elements are
        --Install Button
        --Edit Button
        --Delete Button
        """
        frame = Gtk.Frame()
        grid = Gtk.Grid()
        # grid.set_border_color(style.Color('# 34495E').get_gdk_color())

        # GRID_HEIGHT= 3  # number of rows # not used
        # GRID_WIDTH = 1  # number of columns # not used
        # GRID_BOX_SIZE = 40  # not used
        GRID_ROW_SPACING = 20
        GRID_COLUMN_SPACING = 5

        frame.set_border_width(5)
        frame.add(grid)
        grid.set_column_spacing(GRID_COLUMN_SPACING)
        grid.set_row_spacing(GRID_ROW_SPACING)

        # Install Button
        image_icon = Icon(pixel_size=style.zoom(55 * 1.5),
                          icon_name='install',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.COLOR_WHITE.get_svg())
        installButton = Gtk.Button()
        installButton.set_image(image_icon)
        installButton.modify_bg(Gtk.StateType.NORMAL,
                                style.Color('#34495E').get_gdk_color())
        installButton.props.relief = Gtk.ReliefStyle.NONE
        installButton.connect("clicked", self._clickInstall)
        grid.attach(installButton, 0, 0, 1, 1)

        # Edit Button
        image_icon = Icon(pixel_size=style.MEDIUM_ICON_SIZE,
                          icon_name='edit',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.COLOR_WHITE.get_svg())
        editButton = Gtk.Button()
        editButton.add(image_icon)
        editButton.props.relief = Gtk.ReliefStyle.NONE
        editButton.connect("clicked", self._clickEdit)
        grid.attach(editButton, 0, 1, 1, 1)

        # Delete Button
        image_icon = Icon(pixel_size=style.MEDIUM_ICON_SIZE,
                          icon_name='delete',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.Color('#E74C3C').get_svg())

        deleteButton = Gtk.Button()
        deleteButton.add(image_icon)
        deleteButton.props.relief = Gtk.ReliefStyle.NONE
        deleteButton.connect("clicked", self._clickDelete)
        grid.attach(deleteButton, 0, 2, 1, 1)

        return frame

    def _create_left_toolbar(self):
        """
        This is a vertical toolbar for this page
        Elements are
        --Install Button
        --Edit Button
        --Delete Button
        """
        frame = Gtk.Frame()
        grid = Gtk.Grid()
        # grid.set_border_color(style.Color('# 34495E').get_gdk_color())

        # GRID_HEIGHT= 3  # number of rows
        # GRID_WIDTH = 1  # number of columns
        # GRID_BOX_SIZE = 40
        GRID_ROW_SPACING = 20
        GRID_COLUMN_SPACING = 5

        frame.set_border_width(5)
        frame.add(grid)
        grid.set_column_spacing(GRID_COLUMN_SPACING)
        grid.set_row_spacing(GRID_ROW_SPACING)

        # Install Button
        image_icon = Icon(pixel_size=style.zoom(55 * 1.5),
                          icon_name='install',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.COLOR_WHITE.get_svg())
        installButton = Gtk.Button()
        installButton.set_image(image_icon)
        installButton.modify_bg(Gtk.StateType.NORMAL,
                                style.Color('#34495E').get_gdk_color())
        installButton.props.relief = Gtk.ReliefStyle.NONE
        installButton.connect("clicked", self._clickInstall)
        grid.attach(installButton, 0, 0, 1, 1)

        # Edit Button
        image_icon = Icon(pixel_size=style.MEDIUM_ICON_SIZE,
                          icon_name='edit',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.COLOR_WHITE.get_svg())
        editButton = Gtk.Button()
        editButton.add(image_icon)
        editButton.props.relief = Gtk.ReliefStyle.NONE
        editButton.connect("clicked", self._clickEdit)
        grid.attach(editButton, 0, 1, 1, 1)

        # Delete Button
        image_icon = Icon(pixel_size=style.MEDIUM_ICON_SIZE,
                          icon_name='delete',
                          stroke_color=style.COLOR_BLACK.get_svg(),
                          fill_color=style.Color('#E74C3C').get_svg())

        deleteButton = Gtk.Button()
        deleteButton.add(image_icon)
        deleteButton.props.relief = Gtk.ReliefStyle.NONE
        deleteButton.connect("clicked", self._clickDelete)
        grid.attach(deleteButton, 0, 2, 1, 1)

        return frame

    def _clickDelete(self, handle):
        pass

    def _clickEdit(self, handle):
        globals.SELF.set_page("SUMMARY")

    def _clickInstall(self, handle):
        pass

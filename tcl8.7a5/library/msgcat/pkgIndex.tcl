if {![package vsatisfies [package provide Tcl] 8.7-]} {return}
package ifneeded msgcat 1.7.1 [list source [file join $dir msgcat.tcl]]

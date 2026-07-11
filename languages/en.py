"""
MeshAnalyzer Pro
English Language Pack
"""

TEXT = {
    "app_name": "MeshAnalyzer Pro",

    "dashboard": "Dashboard",
    "mesh_view": "Mesh View",
    "heatmap": "Heatmap",
    "topography": "Topography",
    "surface_3d": "3D View",
    "analysis": "Analysis",
    "diagnosis_recommendations": "Diagnosis and Recommendations",
    "compare": "Compare",
    "history": "History",
    "settings": "Settings",

    "open_conf": "Open Conf. File",
    "project_open": "Open Project",
    "project_save": "Save Project",
    "heatmap_jpg": "Heatmap JPG",
    "topography_jpg": "Topography JPG",
    "surface_3d_jpg": "3D View JPG",
    "pdf": "PDF",
    "export_all": "Export All",

    "toolbar_tooltip_open_conf": (
        "<b>📂 Open Conf. File</b><br>"
        "Opens a mesh, conf, or supported measurement file.<br><br>"
        "After loading, Dashboard, Mesh View, Heatmap, Topography, "
        "3D View, Analysis, and Diagnosis pages are updated automatically."
    ),
    "toolbar_tooltip_project_open": (
        "<b>📁 Open Project</b><br>"
        "Opens a previously saved MeshAnalyzer project file.<br><br>"
        "Saved mesh data and project information are restored."
    ),
    "toolbar_tooltip_project_save": (
        "<b>💾 Save Project</b><br>"
        "Saves the current mesh analysis as a project file.<br><br>"
        "Use it to return to the same analysis data later."
    ),
    "toolbar_tooltip_heatmap_jpg": (
        "<b>🌈 Heatmap JPG</b><br>"
        "Exports the current mesh heatmap as a JPG image.<br><br>"
        "Useful for quickly reviewing high and low regions by color distribution."
    ),
    "toolbar_tooltip_topography_jpg": (
        "<b>〰 Topography JPG</b><br>"
        "Exports the contour/topography view of the mesh surface as a JPG image.<br><br>"
        "Useful for reporting slopes and regional height differences."
    ),
    "toolbar_tooltip_surface_3d_jpg": (
        "<b>🧊 3D View JPG</b><br>"
        "Exports the three-dimensional surface view as a JPG image.<br><br>"
        "Use it to visually present the overall surface shape."
    ),
    "toolbar_tooltip_pdf": (
        "<b>📄 PDF Report</b><br>"
        "Creates a PDF report for the current analysis.<br><br>"
        "The report includes summary values, quality control, charts, and the mesh table."
    ),
    "toolbar_tooltip_export_all": (
        "<b>⬇ Export All</b><br>"
        "Exports the PDF report and supported image outputs into a single folder.<br><br>"
        "Useful for fast reporting and archiving."
    ),
    "toolbar_tooltip_settings": (
        "<b>⚙ Settings</b><br>"
        "Edits tolerance limits, theme, and language options.<br><br>"
        "When saved, related pages are updated automatically."
    ),

    "toolbar_status_open_conf": "Open a mesh or conf file",
    "toolbar_status_project_open": "Open a saved project",
    "toolbar_status_project_save": "Save the current project",
    "toolbar_status_heatmap_jpg": "Export heatmap as JPG",
    "toolbar_status_topography_jpg": "Export topography as JPG",
    "toolbar_status_surface_3d_jpg": "Export 3D view as JPG",
    "toolbar_status_pdf": "Create PDF report",
    "toolbar_status_export_all": "Export all outputs",
    "toolbar_status_settings": "Open settings",

    "ready": "Ready",
    "mesh_waiting": "Waiting for mesh",
    "settings_title": "⚙ MeshAnalyzer Settings",
    "max_total_range": "Total Deviation Limit (mm)",
    "max_rms": "RMS Limit (mm)",
    "max_plane_deviation": "Plane Deviation Limit (mm)",
    "theme": "Theme",
    "language": "Language",
    "save_settings": "💾 Save Settings",
    "success": "Success",
    "settings_saved": "Settings saved.",
    "close": "Close",
    "help": "Help",
    "modules": "Modules",
    "file": "File",
    "view": "View",
    "tools": "Tools",
    "help": "Help",
    "modules": "Modules",
    "about": "About",
    "exit": "Exit",

    "tooltip_quality_status": (
    "<h3>✅ Quality Status</h3>"
    "<b>Description</b><br>"
    "Shows whether the measured mesh values are within the defined tolerance limits.<br><br>"
    "<b>Results</b><br>"
    "🟢 PASS: Values are in the safe range.<br>"
    "🟡 ACCEPTABLE: Values are within the limit but close to it.<br>"
    "🟠 WARNING: Values are above tolerance; check recommended.<br>"
    "🔴 FAIL: Values are outside tolerance.<br><br>"
),

"tooltip_machine_health": (
    "<h3>🩺 Machine Health</h3>"
    "<b>Description</b><br>"
    "An overall performance score ranging from 0 to 100 that summarizes the surface quality.<br><br>"
    "<b>Calculated using</b><br>"
    "• Total Deviation<br>"
    "• RMS<br>"
    "• Plane Deviation<br>"
    "• Smart Diagnostic<br><br>"
    "<b>Interpretation</b><br>"
    "🟢 90–100 : Excellent<br>"
    "🟢 75–89 : Good<br>"
    "🟡 50–74 : Acceptable<br>"
    "🔴 0–49 : Critical<br><br>"
),

    "tooltip_total_range": (
        "<h3>📏 Total Deviation</h3>"
        "<b>Description</b><br>"
        "The height difference between the highest and lowest measured point on the mesh surface.<br><br>"
        "<b>Interpretation</b><br>"
        "Lower values indicate a flatter surface.<br>"
        "Higher values may indicate deformation or warping.<br><br>"
        "<b>Interpretation</b><br>"
        "🟢 0.000–0.120 mm : Excellent<br>"
        "🟢 0.120–0.180 mm : Good<br>"
        "🟡 0.180–0.250 mm : Acceptable<br>"
        "🔴 >0.250 mm : Critical<br><br>"
        "<b>Unit</b><br>mm<br><br>"
    ),

    "tooltip_rms": (
        "<h3>📐 RMS (Root Mean Square)</h3>"
        "<b>Description</b><br>"
        "The square root of the mean of the squared deviations of all measured points from the reference surface.<br><br>"
        "<b>Why is it important?</b><br>"
        "It represents the overall surface quality and is not overly affected by a single extreme point.<br><br>"
        "<b>Interpretation</b><br>"
        "🟢 0.000–0.120 mm : Excellent<br>"
        "🟢 0.120–0.180 mm : Good<br>"
        "🟡 0.180–0.250 mm : Acceptable<br>"
        "🔴 >0.250 mm : Critical<br><br>"
    ),

    "tooltip_plane_deviation": (
        "<h3>📊 Plane Deviation</h3>"
        "<b>Description</b><br>"
        "The maximum distance of the mesh surface from the best-fit reference plane.<br><br>"
        "<b>Typical Applications</b><br>"
        "• Surface flatness<br>"
        "• Mounting alignment<br>"
        "• Twist detection<br><br>"
        "<b>Interpretation</b><br>"
        "Lower values indicate a better aligned surface."
        "<b>Interpretation</b><br>"
        "🟢 0.000–0.120 mm : Excellent<br>"
        "🟢 0.120–0.180 mm : Good<br>"
        "🟡 0.180–0.250 mm : Acceptable<br>"
        "🔴 >0.250 mm : Critical<br><br>"
    ),

    "tooltip_mesh_size": (
        "<h3>📂 Mesh Size</h3>"
        "<b>Description</b><br>"
        "Displays the number of rows and columns in the analyzed mesh.<br><br>"
        "<b>Example</b><br>"
        "20 × 30 = 600 measurement points."
    ),

    "tooltip_minimum": (
        "<h3>⬇ Minimum</h3>"
        "<b>Description</b><br>"
        "The lowest measured value in the mesh.<br><br>"
        "<b>Usage</b><br>"
        "Used in the Total Deviation calculation.<br><br>"
        "<b>Unit</b><br>mm"
    ),

    "tooltip_maximum": (
        "<h3>⬆ Maximum</h3>"
        "<b>Description</b><br>"
        "The highest measured value in the mesh.<br><br>"
        "<b>Usage</b><br>"
        "Used in the Total Deviation calculation.<br><br>"
        "<b>Unit</b><br>mm"
    ),

    "tooltip_average": (
        "<h3>➗ Average</h3>"
        "<b>Description</b><br>"
        "The average height of all measured points.<br><br>"
        "<b>Interpretation</b><br>"
        "Represents the overall reference level of the surface.<br><br>"
        "<b>Unit</b><br>mm"
    ),

    "tooltip_file_info": (
        "<h3>📄 File</h3>"
        "<b>Description</b><br>"
        "Displays the name of the currently loaded mesh file.<br><br>"
        "<b>Additional Information</b><br>"
        "The analysis time is also shown at the bottom of this card."
    ),

    "tooltip_analysis_result": (
        "<h3>🧠 Analysis Result</h3>"
        "<b>Description</b><br>"
        "The overall evaluation generated by the analysis engine after combining all calculated metrics.<br><br>"
        "<b>Possible Results</b><br>"
        "🟢 OK<br>"
        "🟡 Warning<br>"
        "🔴 Requires Inspection<br><br>"
        "<b>Tip</b><br>"
        "This result combines RMS, Total Deviation, Plane Deviation, and Machine Health into a single assessment."
    ),

    "dashboard_title": "MeshAnalyzer Pro Dashboard",

    "machine_health": "Machine Health",
    "quality_status": "Quality Status",
    "total_deviation": "Total Deviation",
    "plane_deviation": "Plane Deviation",
    "mesh_size": "Mesh Size",
    "minimum": "Minimum",
    "maximum": "Maximum",
    "average": "Average",
    "file": "File",
    "analysis": "Analysis",

    "waiting_mesh": "Waiting for mesh",
    "waiting_result": "Waiting for result",
    "no_file": "No file loaded",
    "rows_columns": "Rows × Columns",
    "mesh_average": "Mesh Average",
    "lowest_point": "Lowest Point",
    "highest_point": "Highest Point",

    "tolerance_ok": "Within tolerance",
    "analysis_ok": "OK",
    "mesh_quality_passed": "Mesh passed quality control",
    "near_limit": "Near limit",
    "attention": "Attention",
    "mesh_near_limit": "Mesh is close to tolerance limit",
    "out_of_tolerance": "Out of tolerance",
    "inspection_required": "Inspection Required",
    "mesh_out_of_limits": "Mesh is outside limits",
    "limit": "Limit",
    "lowest_measurement": "Lowest measurement",
    "highest_measurement": "Highest measurement",
    "average_height": "Average height",
    "last_opened_mesh": "Last opened mesh",
    "analysis_time": "Analysis",
    "analysis_empty": "Analysis results will appear here when a mesh is loaded.",
    "analysis_result_for": "Analysis result for {name}",
    "diagnosis_empty": "Diagnosis and recommendations will appear here when a mesh is loaded.",
    "diagnosis_result_for": "Diagnosis and recommendations for {name}",
    "analysis_duration": "Analysis Duration",
    "analysis_calculation_time": "Calculation time",
    "overall_status": "Overall Status",
    "geometry_section": "Plane and Geometry",
    "quality_control": "Quality Control",
    "standard_deviation": "Standard Deviation",
    "plane_max_deviation": "Plane Max Deviation",
    "plane_rms_deviation": "Plane RMS Deviation",
    "x_slope": "X Slope",
    "y_slope": "Y Slope",
    "trend": "Trend Analysis",
    "smart_diagnostic": "Smart Diagnostic",
    "mechanical_diagnostic": "Mechanical Diagnostic",
    "status_pass": "PASS",
    "status_ok": "OK",
    "status_excellent": "EXCELLENT",
    "status_good": "GOOD",
    "status_warning": "WARNING",
    "status_fail": "FAIL",
    "status_error": "ERROR",
    "status_bad": "BAD",
    "status_critical": "CRITICAL",


    "trend_no_data": "Insufficient data",
    "trend_improving": "Improving",
    "trend_degrading": "Degrading",
    "trend_stable": "Stable",
    "trend_min_records_required": "At least 2 records are required for trend analysis.",
    "trend_record_count": "Record Count",
    "trend_status": "Status",
    "trend_first_total_deviation": "First Total Deviation",
    "trend_last_total_deviation": "Last Total Deviation",
    "trend_first_rms": "First RMS",
    "trend_last_rms": "Last RMS",
    "trend_change": "Change",

    "critical": "Critical",
    "good": "Good",
    "excellent": "Excellent",
    "needs_attention": "Needs Attention",

    "mesh_summary": "Mesh View",
    "selected_point": "Selected Point",
    "selected_point_none": "Selected Point: -",
    "point_status": "Status",
    "normal_point": "Normal Point",
    "minimum_point": "Minimum Point",
    "maximum_point": "Maximum Point",

    "tooltip_mesh_summary": (
        "<h3>Mesh View</h3>"

        "<b>Size</b><br>"
        "Displays the number of rows and columns of the mesh.<br><br>"

        "<b>Minimum</b><br>"
        "Lowest measured height.<br><br>"

        "<b>Maximum</b><br>"
        "Highest measured height.<br><br>"

        "<b>Average</b><br>"
        "Average height of all measured points.<br><br>"

        "<b>RMS</b><br>"
        "Most important statistical indicator of surface quality.<br><br>"

        "<b>Total Deviation</b><br>"
        "Difference between maximum and minimum height."
    ),

        "color_scale": "Color Scale",
        "color_palette": "Color Palette:",
        "heatmap_summary": "Heatmap",

        "heatmap_summary_tooltip": (
        "<b>Heatmap</b><br><br>"

        "This panel summarizes the color distribution and key statistics "
        "of the measured mesh data.<br><br>"

        "<b>🎨 Color Palette</b><br>"
        "Select the color palette used for the heatmap. "
        "Changing the palette affects only the visualization, not the measurement data.<br><br>"

        "<b>📉 Minimum</b><br>"
        "The lowest measured Z value.<br><br>"

        "<b>📈 Maximum</b><br>"
        "The highest measured Z value.<br><br>"

        "<b>📊 Average</b><br>"
        "The average height of all measured points.<br><br>"

        "<b>📐 RMS</b><br>"
        "A statistical value representing overall surface irregularity. "
        "Lower RMS indicates a flatter surface.<br><br>"

        "<b>📏 Total Deviation</b><br>"
        "The total difference between the highest and lowest point.<br><br>"

        "<b>💡 Tips</b><br>"
        "• Hovering over a cell highlights its border.<br>"
        "• The same value is marked on the color scale.<br>"
        "• Different color palettes only change the visual presentation."
    ),

}

TEXT.update({
    "surface_summary": "3D View",
    "surface_view_angle": "View Angle:",
    "surface_view_default": "Default",
    "surface_view_front": "Front",
    "surface_view_side": "Side",
    "surface_view_top": "Top",
    "surface_view_detail": "Detail",
    "surface_matrix_mode": "Matrix",
    "surface_probed_matrix": "Probed matrix",
    "surface_mesh_matrix": "Mesh matrix",
    "surface_wireframe": "Wireframe",
    "surface_zero_plane": "Show surface plane",
    "surface_color_scale": "Color scale",
    "surface_box_scale": "Box scale",
    "surface_reset_color_scale": "Reset color scale to default",
    "surface_reset_box_scale": "Reset box scale to default",
    "surface_measurement": "Measurement",
    "surface_real_x": "Real X",
    "surface_real_y": "Real Y",
    "surface_color_scale_position": "Color scale",
    "surface_summary_tooltip": (
        "<b>3D View</b><br><br>"
        "Shows the measured bed mesh as a three-dimensional surface. "
        "Use it to inspect tilt, low/high regions, and overall surface shape."
    ),
    "surface_minimum_tooltip": (
        "<b>Minimum</b><br><br>"
        "The lowest measured Z value in the current mesh."
    ),
    "surface_maximum_tooltip": (
        "<b>Maximum</b><br><br>"
        "The highest measured Z value in the current mesh."
    ),
    "surface_average_tooltip": (
        "<b>Average</b><br><br>"
        "The average Z height of all measurement points."
    ),
    "surface_rms_tooltip": (
        "<b>RMS</b><br><br>"
        "A surface irregularity indicator. Lower RMS means a flatter measured surface."
    ),
    "surface_total_range_tooltip": (
        "<b>Total Deviation</b><br><br>"
        "The difference between the highest and lowest measured point."
    ),
    "topography_summary": "Topography",
    "contour_levels": "Contour Levels:",
    "topography_summary_tooltip": (
        "<b>Topography</b><br><br>"
        "This panel helps interpret the mesh surface with equal-height contour "
        "lines.<br><br>"
        "<b>Color Palette</b><br>"
        "Changes the color distribution used on the map. Measurement data is not changed.<br><br>"
        "<b>Contour Levels</b><br>"
        "Controls the detail density of height bands and contour lines. "
        "Higher values show more detail; lower values create a simpler view."
    ),
    "history_title": "History",
    "history_tooltip": (
        "<b>History</b><br><br>"
        "Lists mesh files opened before. "
        "Double-click a record, or select and open it, to load it again."
    ),
    "history_info": (
        "Previously opened mesh records are kept here. "
        "Double-click a row to open it again, delete the selected record, "
        "or clear the entire history."
    ),
    "history_refresh": "Refresh History",
    "history_open_selected": "Open Selected",
    "history_delete_selected": "Delete Selected",
    "history_clear": "Clear History",
    "history_id": "ID",
    "history_date": "Date",
    "history_file": "File",
    "history_rows": "Rows",
    "history_cols": "Columns",
    "history_empty": "No history records.",
    "history_record_count": "{count} records listed.",
    "history_load_failed_title": "Mesh Not Found",
    "history_load_failed_message": "The selected history record could not be loaded.",
    "history_delete_title": "Delete Record",
    "history_delete_message": "Delete the selected history record?",
    "history_clear_title": "Clear History",
    "history_clear_message": "Permanently delete the entire history?",
})

TEXT.update({
    "message": "Message",
    "general_assessment": "General Assessment",
    "no_mechanical_issue": "No significant mechanical issue detected.",
    "corner_analysis": "Corner Analysis",
    "lowest_corner": "Lowest corner",
    "highest_corner": "Highest corner",
    "corner_front_left": "Front Left",
    "corner_front_right": "Front Right",
    "corner_rear_left": "Rear Left",
    "corner_rear_right": "Rear Right",
    "slope_analysis": "Slope Analysis",
    "x_direction": "X Direction",
    "y_direction": "Y Direction",
    "x_axis_balanced": "X axis is balanced",
    "y_axis_balanced": "Y axis is balanced",
    "right_higher_than_left": "Right side is higher than left",
    "left_higher_than_right": "Left side is higher than right",
    "rear_higher_than_front": "Rear side is higher than front",
    "front_higher_than_rear": "Front side is higher than rear",
    "twist_analysis": "Twist Analysis",
    "twist_value": "Twist Value",
    "direction": "Direction",
    "severity": "Severity",
    "no_significant_twist": "No significant twist",
    "clockwise_twist": "Clockwise twist tendency",
    "counter_clockwise_twist": "Counter-clockwise twist tendency",
    "severity_none": "None",
    "severity_light": "Light",
    "severity_medium": "Medium",
    "severity_high": "High",
    "shim_recommendations": "Shim Recommendations",
    "shim_no_change": "No change required",
    "shim_add_raise": "Add shim / raise",
    "shim_reduce_lower": "Reduce shim / lower",
    "main_recommendation": "Main Recommendation",
    "main_recommendation_sentence": "About {delta} mm correction is recommended for {name}.",
    "action": "Action",
    "recommended_action": "Recommended Action",
    "remeasure_after_adjustment": "Take a new mesh measurement after mechanical adjustment.",
    "apply_largest_shim_first": "Apply the largest shim recommendation first.",
    "run_auto_level_again": "Then run automatic leveling again.",
    "mesh_within_tolerance": "Mesh is within tolerance.",
    "mesh_near_tolerance": "Mesh is close to the limit.",
    "mesh_out_of_tolerance": "Mesh is outside tolerance.",
    "table_almost_flat": "The bed is almost completely flat.",
    "table_good_condition": "The bed is in good condition.",
    "table_slight_warp": "Slight bed warping is present.",
    "table_serious_warp": "The bed is seriously warped.",
    "x_right_side_high": "The right side is higher on the X axis.",
    "x_left_side_high": "The left side is higher on the X axis.",
    "surface_very_smooth": "The surface is very smooth.",
    "surface_acceptable": "The surface is acceptable.",
    "surface_local_waves": "Local surface waves are present.",
    "surface_serious_deformation": "The surface shows serious deformation.",
    "recommendations": "Recommendations",
    "raise": "Raise",
    "lower": "Lower",
    "compare_open_old": "Open Old Mesh",
    "compare_open_new": "Open New Mesh",
    "compare_action": "Compare",
    "compare_old_mesh": "Old Mesh",
    "compare_new_mesh": "New Mesh",
    "compare_old_label": "Old",
    "compare_new_label": "New",
    "compare_old_not_selected": "Old mesh not selected",
    "compare_new_not_selected": "New mesh not selected",
    "compare_no_previous_short": "No previous history record",
    "compare_auto_hint": "Comparison runs automatically when two meshes are selected.",
    "compare_no_previous_history": "No previous mesh record was found in history for comparison.",
    "compare_select_two_mesh": "Please select two mesh files.",
    "compare_open_old_title": "Open Old Mesh",
    "compare_open_new_title": "Open New Mesh",
    "mesh_file_filter": "Mesh Files (*.pack *.csv *.txt *.json);;All Files (*)",
    "compare_report_title": "MESH COMPARISON",
    "compare_old_total_deviation": "Old Total Deviation",
    "compare_new_total_deviation": "New Total Deviation",
    "compare_improvement": "Improvement",
    "compare_delta_min": "Delta Min",
    "compare_delta_max": "Delta Max",
    "compare_delta_average": "Delta Average",
    "compare_delta_mesh": "Delta Mesh",
    "compare_delta_heatmap": "Difference Map",
    "compare_cell_value": "Value",
    "compare_cell_difference": "Difference",
})


TEXT.update({
    "report_title": "MeshAnalyzer Pro Report",
    "report_date": "Date",
    "report_file": "File",
    "report_mesh_summary_section": "Mesh Summary",
    "report_geometry_section": "Geometry Analysis",
    "report_machine_health_section": "Machine Health Score",
    "report_heatmap_section": "Heatmap",
    "report_topography_section": "Topographic Map",
    "report_surface_section": "3D Surface",
    "report_smart_diagnostic_section": "Smart Diagnostic",
    "report_mechanical_diagnostic_section": "Mechanical Diagnostic",
    "report_mesh_table_section": "Mesh Table",
    "report_heatmap_title": "Heatmap",
    "report_topography_title": "Topographic Map",
    "report_surface_title": "3D Surface",
    "report_x_coordinate": "X Coordinate",
    "report_y_coordinate": "Y Coordinate",
    "report_height_mm": "Height (mm)",
    "report_score": "Score",
    "report_status": "Status",
    "report_category": "Category",
})

TEXT.update({
    "export_mesh_required_message": "Open a mesh file first.",
    "export_pdf_failed_title": "PDF Could Not Be Created",
    "export_pdf_save_title": "Save PDF Report",
    "export_pdf_error_title": "PDF Error",
    "export_pdf_created_status": "PDF created: {filename}",
    "export_pdf_failed_status": "PDF could not be created.",
    "export_jpeg_failed_title": "JPEG Could Not Be Created",
    "export_heatmap_jpeg_save_title": "Save Heatmap JPEG",
    "export_topography_jpg_save_title": "Save Topography JPG",
    "export_surface_jpg_save_title": "Save 3D View JPG",
    "export_jpeg_error_title": "JPEG Error",
    "export_jpeg_created_status": "JPEG created: {filename}",
    "export_jpeg_failed_status": "JPEG could not be created.",
})


TEXT.update({
    "tooltip_analysis_overall_status": (
        "<h3>✅ Overall Status</h3>"
        "Shows the overall pass/fail result based on the configured tolerance limits.<br><br>"
        "FAIL means that at least one quality-control limit has been exceeded."
    ),
    "tooltip_analysis_duration": (
        "<h3>⏱ Analysis Duration</h3>"
        "Shows how long the analysis engine took to process the mesh data.<br><br>"
        "This is a performance indicator and does not directly affect measurement quality."
    ),
    "tooltip_analysis_mesh_summary": (
        "<h3>📊 Mesh Summary</h3>"
        "Shows key statistics such as mesh size, minimum, maximum, average, RMS and total deviation.<br><br>"
        "Use this section for a quick overview of the measured surface."
    ),
    "tooltip_analysis_geometry": (
        "<h3>📐 Plane and Geometry</h3>"
        "Shows the surface slope, plane RMS deviation and maximum deviation from the reference plane.<br><br>"
        "It helps identify bed warping, mounting issues or surface twist."
    ),
    "tooltip_analysis_quality_control": (
        "<h3>🧪 Quality Control</h3>"
        "Compares total deviation, RMS and plane deviation against the limits defined in Settings.<br><br>"
        "Red indicates a failed limit, yellow indicates a near-limit warning, and green indicates acceptable values."
    ),
    "tooltip_analysis_trend": (
        "<h3>📈 Trend</h3>"
        "Shows trend information compared with previous mesh records when history data is available.<br><br>"
        "At least two records are required for trend analysis."
    ),
    "tooltip_diagnosis_smart": (
        "<h3>🧠 Smart Diagnostic</h3>"
        "A summarized diagnosis generated by interpreting the mesh statistics.<br><br>"
        "Use it to quickly understand the likely surface condition, risk level and overall result."
    ),
    "tooltip_diagnosis_mechanical": (
        "<h3>🛠 Mechanical Diagnostic</h3>"
        "Lists possible mechanical causes and practical recommendations based on the mesh behavior.<br><br>"
        "It helps interpret bed leveling, looseness, warping or alignment problems."
    ),
    "tooltip_compare_old_mesh": (
        "<h3>⬅ Old Mesh</h3>"
        "Displays the previous mesh used as the comparison reference.<br><br>"
        "The difference calculation is based on this mesh."
    ),
    "tooltip_compare_new_mesh": (
        "<h3>➡ New Mesh</h3>"
        "Displays the current or newly loaded mesh data.<br><br>"
        "It is compared against the old mesh to calculate improvement or degradation."
    ),
    "tooltip_compare_report": (
        "<h3>📋 Mesh Comparison</h3>"
        "Summarizes total deviation, improvement ratio and delta values between the old and new mesh.<br><br>"
        "Positive and negative changes show how the surface has shifted."
    ),
    "tooltip_compare_delta_heatmap": (
        "<h3>🌡 Delta Heatmap</h3>"
        "Shows cell-by-cell differences between the new mesh and the old mesh using colors.<br><br>"
        "Values close to zero indicate little change; larger positive or negative values indicate significant change."
    ),
})



TEXT.update({
    "empty_conf_waiting_title": "Waiting for conf file",
    "empty_conf_waiting_message": "This area will be updated automatically after opening a mesh or conf file.",
    "compare_old_total_range": "Old Total Deviation",
    "compare_new_total_range": "New Total Deviation",
    "reset_to_default": "Reset Default",
    "settings_applied": "Settings applied",
    "settings_total_deviation_limit_tooltip": "<b>Total Deviation Limit</b><br><br>Limits the total difference between the highest and lowest measured mesh point. Useful for quickly judging overall bed height variation.<br><br><b>Excellent:</b> ≤ 0.300 mm<br><b>Good:</b> ≤ 0.450 mm<br><b>Acceptable:</b> ≤ 0.600 mm<br><b>Critical:</b> &gt; 0.600 mm",
    "settings_rms_limit_tooltip": "<b>RMS Limit</b><br><br>Represents the overall surface irregularity of all mesh points statistically. A lower RMS value means the surface is generally more stable and flatter.<br><br><b>Excellent:</b> ≤ 0.120 mm<br><b>Good:</b> ≤ 0.180 mm<br><b>Acceptable:</b> ≤ 0.250 mm<br><b>Critical:</b> &gt; 0.250 mm",
    "settings_plane_deviation_limit_tooltip": "<b>Plane Deviation Limit</b><br><br>Limits how far the mesh surface deviates from the ideal fitted plane. Useful for checking bed tilt, mechanical alignment and planar distortion.<br><br><b>Excellent:</b> ≤ 0.150 mm<br><b>Good:</b> ≤ 0.220 mm<br><b>Acceptable:</b> ≤ 0.300 mm<br><b>Critical:</b> &gt; 0.300 mm",
    "settings_graph_defaults": "Graph Defaults",
    "settings_default_heatmap_palette": "Default Heatmap Palette",
    "settings_default_topography_palette": "Default Topography Palette",
    "settings_default_surface_palette": "Default 3D Surface Palette",
    "settings_default_surface_view": "Default 3D View Angle",
    "settings_report_settings": "Report Settings",
    "settings_report_include_graphs": "Include charts in PDF report",
    "settings_report_include_diagnostics": "Include diagnostics and recommendations in PDF report",
    "settings_report_include_mesh_table": "Include mesh table in PDF report",
    "settings_export_jpg_show_cell_values": "Show cell values in JPG heatmap",
    "settings_appearance_settings": "Appearance Settings",
    "settings_appearance_show_table_values": "Show values in table cells",
    "settings_appearance_show_colorbar": "Show colorbar in charts",
    "settings_appearance_show_hover_info": "Show hover info popups",
    "settings_appearance_start_maximized": "Start window maximized",
    "dashboard_disclaimer": "<b>Disclaimer:</b> The software is based on mathematical calculations. Any physical adjustments you make on the device (screwing, adding shims, etc.) are the user's responsibility.",
    "settings_tolerance_settings": "Tolerance Settings",
    "settings_general_settings": "General Settings",
    "mechanical_priority_recommendations": "Priority Mechanical Recommendations",
    "no_priority_correction_needed": "No priority mechanical correction is required.",
    "apply_largest_correction_first": "Start with the largest correction first:",
    "compare_summary_section": "Result Summary",
    "compare_metric_changes": "Metric Changes",
    "compare_total_range_change": "Total Deviation Change",
    "compare_old_rms": "Old RMS",
    "compare_new_rms": "New RMS",
    "compare_rms_change": "RMS Change",
    "compare_regional_changes": "Regional Changes",
    "compare_most_improved_area": "Most improved area",
    "compare_most_worsened_area": "Most worsened area",
    "compare_delta_statistics": "Delta Statistics",
    "compare_delta_abs_max": "Delta Absolute Maximum",
    "compare_summary_better": "Overall result: the new mesh appears improved compared with the previous measurement.",
    "compare_summary_worse": "Overall result: the new mesh appears worse compared with the previous measurement.",
    "compare_summary_similar": "Overall result: the new mesh is close to the previous measurement; improvement or worsening is limited.",
    "report_result_summary_section": "Result Summary",
    "report_summary_general_status": "General Status",
    "report_summary_score": "Health Score",
    "report_summary_tolerance": "Tolerance Status",
    "report_summary_main_problem": "Main Problem",
    "report_summary_recommended_action": "Recommended Action",
    "report_summary_status_good": "Good / Acceptable",
    "report_summary_status_warning": "Needs Attention",
    "report_summary_status_critical": "Critical / Check Required",
    "report_summary_problem_tolerance": "Mesh values are outside the configured tolerance limits.",
    "report_summary_problem_plane": "Plane deviation appears high.",
    "report_summary_problem_x_slope": "There is a noticeable slope in the X direction.",
    "report_summary_problem_y_slope": "There is a noticeable slope in the Y direction.",
    "report_summary_problem_none": "No clear main problem was detected.",
    "report_summary_recommendation_shim": "Approximately {delta:.3f} mm correction is recommended for {name}.",
    "report_summary_recommendation_remeasure": "Take a new mesh measurement after mechanical inspection.",
    "history_favorite": "Favorite",
    "history_label": "Label",
    "history_note": "Note",
    "history_toggle_favorite": "⭐ Favorite",
    "history_edit_note_label": "Note / Label",
    "history_compare_previous": "Compare Previous",
    "history_edit_label_title": "Measurement Label",
    "history_edit_label_message": "Enter a short label for this measurement:",
    "history_edit_note_title": "Measurement Note",
    "history_edit_note_message": "Enter a note for this measurement:",
    "history_no_previous_for_compare": "No previous mesh record was found for this item.",
    "mesh_validation_info": "When a file is opened, mesh data is checked for empty data, row/column consistency, numeric values, and unusually large value ranges.",
    "coordinate_standard_info": "<b>Coordinate Standard:</b> Front Left = X1/Y1 · Front Right = Xmax/Y1 · Rear Left = X1/Ymax · Rear Right = Xmax/Ymax",
    "acceptable": "Acceptable",
    "status_acceptable": "ACCEPTABLE",
    "acceptable_range": "Within acceptable range",
    "mesh_quality_acceptable": "Mesh is within the acceptable range",
    "check_recommended": "Check recommended",
    "mesh_check_recommended": "Mesh is above tolerance; check recommended",
    "conf_help_card_title": "How to Get Conf. File",
    "conf_help_wiki_button": "Anycubic Wiki",
    "conf_help_device_button": "2. From Device",
    "conf_help_wiki_title": "Get Conf. File via Anycubic Wiki",
    "conf_help_wiki_message": "Open this page: https://wiki.anycubic.com/en/fdm-3d-printer/kobra-s1-combo/fault-log-export\\n\\nFollow the steps on the page, then open the AC_CONF.pack file from the USB drive.\\n\\nWARNING: Do not use AC_LOG.pack with this method!",
    "conf_help_device_title": "Get Conf. File from Device",
    "conf_help_device_message": "Insert a USB drive into the printer, then follow this path on the printer screen: Setting - Device - Export logs to U-Disk.\\n\\nInsert the USB drive into your computer and open AC_LOG.pack.",
    "dialog_ok": "OK",
    "dialog_cancel": "Cancel",
    "dialog_yes": "Yes",
    "dialog_no": "No",
    "dialog_open": "Open",
    "dialog_save": "Save",
    "history_edit_label_button": "Label",
    "history_edit_note_button": "Note",
    "report_mesh_table_coordinate_note": "Coordinates: Front Left = X1/Y1 · Front Right = Xmax/Y1 · Rear Left = X1/Ymax · Rear Right = Xmax/Ymax",
})

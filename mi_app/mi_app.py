"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.style(
            """
            @font-face {
                font-family: 'LucideIcons';
                src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
            }
        """
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.flex(
                        rx.box(
                            "DataBlast Consulting",
                            font_weight="700",
                            font_size="1.5rem",
                            line_height="2rem",
                            color="#1D4ED8",
                        ),
                        rx.box(
                            rx.el.a(
                                "Home",
                                href="#home",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.el.a(
                                "About Us",
                                href="#about",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.el.a(
                                "Services",
                                href="#services",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.el.a(
                                "Case Studies",
                                href="#case-studies",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.el.a(
                                "Blog",
                                href="#blog",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.el.a(
                                "Contact",
                                href="#contact",
                                transition_duration="300ms",
                                _hover={"color": "#1D4ED8"},
                                color="#4B5563",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            display=rx.breakpoints({"0px": "none", "768px": "flex"}),
                            column_gap="1.5rem",
                        ),
                        rx.box(
                            rx.icon(
                                tag="menu", height="1.5rem", color="#4B5563", width="1.5rem"
                            ),
                            display=rx.breakpoints({"768px": "none"}),
                        ),
                        display="flex",
                        align_items="center",
                        justify_content="space-between",
                    ),
                    width="100%",
                    style=rx.breakpoints(
                        {
                            "640px": {"max-width": "640px"},
                            "768px": {"max-width": "768px"},
                            "1024px": {"max-width": "1024px"},
                            "1280px": {"max-width": "1280px"},
                            "1536px": {"max-width": "1536px"},
                        }
                    ),
                    margin_left="auto",
                    margin_right="auto",
                    padding_left=rx.breakpoints(
                        {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                    ),
                    padding_right=rx.breakpoints(
                        {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                    ),
                    padding_top="1rem",
                    padding_bottom="1rem",
                ),
                background_color="#ffffff",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                position="sticky",
                width="100%",
                z_index="10",
            ),
            rx.box(
                rx.box(
                    rx.box(
                        rx.heading(
                            "Revolutionizing Blasting Technology",
                            font_weight="700",
                            margin_bottom="1.5rem",
                            font_size=rx.breakpoints({"0px": "2.25rem", "640px": "3rem"}),
                            line_height=rx.breakpoints({"0px": "2.5rem", "640px": "1"}),
                            as_="h1",
                        ),
                        rx.text(
                            "DataBlast Consulting: Your partner in precision blasting and vibration monitoring for optimized mining and construction processes",
                            max_width="48rem",
                            margin_bottom="2.5rem",
                            margin_left="auto",
                            margin_right="auto",
                            font_size="1.25rem",
                            line_height="1.75rem",
                        ),
                        rx.el.a(
                            "Schedule a Consultation",
                            href="#contact",
                            background_color="#ffffff",
                            transition_duration="300ms",
                            font_weight="600",
                            _hover={"background-color": "#EFF6FF"},
                            display="inline-block",
                            padding_left="2rem",
                            padding_right="2rem",
                            padding_top="0.75rem",
                            padding_bottom="0.75rem",
                            border_radius="9999px",
                            color="#1D4ED8",
                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        text_align="center",
                    ),
                    class_name="bg-gradient-to-r from-blue-700 to-blue-900",
                    id="home",
                    padding_top="6rem",
                    padding_bottom="6rem",
                    color="#ffffff",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "About DataBlast Consulting",
                            font_weight="700",
                            margin_bottom="4rem",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            text_align="center",
                            as_="h2",
                        ),
                        rx.flex(
                            rx.box(
                                rx.image(
                                    alt="DataBlast Consulting team working on-site with advanced equipment",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/rMYnD6p8iRIgAhwp9u58DUrBvtLe9ovHyQ9JKW3eJQgTUQhTA/out-0.webp",
                                    border_radius="0.5rem",
                                    box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
                                    width="100%",
                                ),
                                margin_bottom=rx.breakpoints(
                                    {"0px": "2.5rem", "1024px": "0"}
                                ),
                                padding_right=rx.breakpoints({"1024px": "2.5rem"}),
                                width=rx.breakpoints({"1024px": "50%"}),
                            ),
                            rx.box(
                                rx.heading(
                                    "Our Mission",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    font_size="1.5rem",
                                    line_height="2rem",
                                    color="#1D4ED8",
                                    as_="h3",
                                ),
                                rx.text(
                                    "To revolutionize the mining and construction industries through cutting-edge blasting technology and data-driven solutions, enhancing safety, efficiency, and environmental stewardship.",
                                    margin_bottom="1.5rem",
                                    color="#4B5563",
                                ),
                                rx.heading(
                                    "Our Vision",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    font_size="1.5rem",
                                    line_height="2rem",
                                    color="#1D4ED8",
                                    as_="h3",
                                ),
                                rx.text(
                                    "To be the global leader in precision blasting and vibration monitoring, driving innovation and setting new industry standards for performance and sustainability.",
                                    margin_bottom="1.5rem",
                                    color="#4B5563",
                                ),
                                width=rx.breakpoints({"1024px": "50%"}),
                            ),
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "1024px": "row"}
                            ),
                            align_items="center",
                            margin_bottom="4rem",
                        ),
                        rx.box(
                            rx.heading(
                                "Our Core Values",
                                font_weight="700",
                                margin_bottom="2rem",
                                font_size="1.5rem",
                                line_height="2rem",
                                color="#1D4ED8",
                                text_align="center",
                                as_="h3",
                            ),
                            rx.box(
                                rx.box(
                                    rx.icon(
                                        alt="Innovation icon",
                                        tag="lightbulb",
                                        height="4rem",
                                        margin_bottom="1rem",
                                        margin_left="auto",
                                        margin_right="auto",
                                        width="4rem",
                                    ),
                                    rx.heading(
                                        "Innovation",
                                        font_weight="700",
                                        margin_bottom="0.5rem",
                                        font_size="1.125rem",
                                        line_height="1.75rem",
                                        as_="h4",
                                    ),
                                    rx.text(
                                        "Continuously pushing the boundaries of blasting technology",
                                        color="#4B5563",
                                    ),
                                    text_align="center",
                                ),
                                rx.box(
                                    rx.icon(
                                        alt="Safety icon",
                                        tag="shield",
                                        height="4rem",
                                        margin_bottom="1rem",
                                        margin_left="auto",
                                        margin_right="auto",
                                        width="4rem",
                                    ),
                                    rx.heading(
                                        "Safety",
                                        font_weight="700",
                                        margin_bottom="0.5rem",
                                        font_size="1.125rem",
                                        line_height="1.75rem",
                                        as_="h4",
                                    ),
                                    rx.text(
                                        "Prioritizing the well-being of our team and clients above all else",
                                        color="#4B5563",
                                    ),
                                    text_align="center",
                                ),
                                rx.box(
                                    rx.icon(
                                        alt="Sustainability icon",
                                        tag="leaf",
                                        height="4rem",
                                        margin_bottom="1rem",
                                        margin_left="auto",
                                        margin_right="auto",
                                        width="4rem",
                                    ),
                                    rx.heading(
                                        "Sustainability",
                                        font_weight="700",
                                        margin_bottom="0.5rem",
                                        font_size="1.125rem",
                                        line_height="1.75rem",
                                        as_="h4",
                                    ),
                                    rx.text(
                                        "Committed to environmentally responsible blasting practices",
                                        color="#4B5563",
                                    ),
                                    text_align="center",
                                ),
                                gap="2rem",
                                display="grid",
                                grid_template_columns=rx.breakpoints(
                                    {
                                        "0px": "repeat(1, minmax(0, 1fr))",
                                        "768px": "repeat(3, minmax(0, 1fr))",
                                    }
                                ),
                            ),
                            background_color="#F3F4F6",
                            padding="2.5rem",
                            border_radius="0.75rem",
                            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                    ),
                    id="about",
                    background_color="#ffffff",
                    padding_top="5rem",
                    padding_bottom="5rem",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Our Comprehensive Services",
                            font_weight="700",
                            margin_bottom="4rem",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color="#1D4ED8",
                            text_align="center",
                            as_="h2",
                        ),
                        rx.box(
                            rx.box(
                                rx.image(
                                    alt="Advanced seismograph monitoring blast vibrations",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/UiOfO24LVHSCfkafc9UZKQrc4PKhYQ4E05FYyqpYhM3nogCnA/out-0.webp",
                                    height="14rem",
                                    margin_bottom="1.5rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Precision Shot Measurement",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Utilizing state-of-the-art seismographs and accelerometers to capture high-resolution data on blast vibrations, air overpressure, and fragment velocity. Our advanced analytics provide real-time insights for immediate optimization.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.list(
                                    rx.el.li(
                                        "High-frequency sampling rates up to 16,000 Hz"
                                    ),
                                    rx.el.li("Multi-channel waveform analysis"),
                                    rx.el.li(
                                        "Near-field and far-field monitoring capabilities"
                                    ),
                                    list_style_type="disc",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                background_color="#ffffff",
                                transition_duration="300ms",
                                _hover={
                                    "box-shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
                                },
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.box(
                                rx.image(
                                    alt="3D laser scanning of a quarry face for precise blast design",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/qL6RB85f1c3WUidf95CIfavmUJ1W7CYPcuUjypMg9KNmogCnA/out-0.webp",
                                    height="14rem",
                                    margin_bottom="1.5rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Advanced 3D Projection and Modeling",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Harnessing the power of LiDAR and photogrammetry to create highly accurate 3D models of blast sites. Our proprietary software integrates geological data for unparalleled blast design precision.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.list(
                                    rx.el.li("Sub-centimeter accuracy in face profiling"),
                                    rx.el.li("Integration with drill navigation systems"),
                                    rx.el.li("Automated burden and spacing calculations"),
                                    list_style_type="disc",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                background_color="#ffffff",
                                transition_duration="300ms",
                                _hover={
                                    "box-shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
                                },
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.box(
                                rx.image(
                                    alt="Engineers using advanced software for blast design optimization",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/l2IXzlEkk4ZeUiTemP5GcWxK6dLiz9uD8qxCeiW4fmxPRBFOB/out-0.webp",
                                    height="14rem",
                                    margin_bottom="1.5rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Drill and Blast Design Optimization",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Leveraging machine learning algorithms to analyze historical blast data and geological information, our team develops custom-tailored drill and blast designs that maximize fragmentation while minimizing unwanted effects.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.list(
                                    rx.el.li("AI-driven pattern optimization"),
                                    rx.el.li("Customized energy distribution models"),
                                    rx.el.li("Fragmentation prediction and analysis"),
                                    list_style_type="disc",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                background_color="#ffffff",
                                transition_duration="300ms",
                                _hover={
                                    "box-shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
                                },
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            rx.box(
                                rx.image(
                                    alt="Consultant performing a comprehensive audit of blasting operations and safety protocols",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/XYBzDEoPMl7eXqi3UPIykecHNIMfVzreIODSJY1HlIdORBFOB/out-0.webp",
                                    height="14rem",
                                    margin_bottom="1.5rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Comprehensive Blasting Audits",
                                    font_weight="700",
                                    margin_bottom="1rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Our expert consultants conduct thorough evaluations of your entire blasting process, from explosives handling to post-blast analysis. We identify areas for improvement in safety, efficiency, and regulatory compliance.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.list(
                                    rx.el.li("Risk assessment and mitigation strategies"),
                                    rx.el.li(
                                        "Compliance checks with local and international standards"
                                    ),
                                    rx.el.li(
                                        "Performance benchmarking against industry best practices"
                                    ),
                                    list_style_type="disc",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                background_color="#ffffff",
                                transition_duration="300ms",
                                _hover={
                                    "box-shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
                                },
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                                transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                            ),
                            gap="2.5rem",
                            display="grid",
                            grid_template_columns=rx.breakpoints(
                                {
                                    "0px": "repeat(1, minmax(0, 1fr))",
                                    "768px": "repeat(2, minmax(0, 1fr))",
                                }
                            ),
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                    ),
                    id="services",
                    background_color="#F3F4F6",
                    padding_top="5rem",
                    padding_bottom="5rem",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Case Studies",
                            font_weight="700",
                            margin_bottom="4rem",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color="#1D4ED8",
                            text_align="center",
                            as_="h2",
                        ),
                        rx.box(
                            rx.box(
                                rx.heading(
                                    "Optimizing Quarry Operations",
                                    font_weight="700",
                                    margin_bottom="1.5rem",
                                    font_size="1.5rem",
                                    line_height="2rem",
                                    color="#1D4ED8",
                                    as_="h3",
                                ),
                                rx.flex(
                                    rx.image(
                                        alt="Before: Uneven fragmentation and excessive flyrock",
                                        src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/7TxCv0liQrq6AVrsqlXroLkMs9EOi96eCcBwXU4fBfwqtgCnA/out-0.webp",
                                        height="12rem",
                                        object_fit="cover",
                                        border_radius="0.5rem",
                                        width="50%",
                                    ),
                                    rx.image(
                                        alt="After: Uniform fragmentation and controlled blast",
                                        src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/OemgedW7H4pueIpsdX3mDxDJwsbJ4k69kuu7DM3JmN3rtgCnA/out-0.webp",
                                        height="12rem",
                                        object_fit="cover",
                                        border_radius="0.5rem",
                                        width="50%",
                                    ),
                                    display="flex",
                                    margin_bottom="1.5rem",
                                    column_gap="1rem",
                                ),
                                rx.text(
                                    rx.text.strong("Client:", color="#1F2937"),
                                    " Mountain Ridge Aggregates",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    rx.text.strong("Challenge:", color="#1F2937"),
                                    " Inconsistent fragmentation and excessive flyrock issues",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    rx.text.strong("Solution:", color="#1F2937"),
                                    " Implemented 3D laser scanning and AI-driven blast design optimization",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    "Results:",
                                    font_weight="600",
                                    margin_bottom="0.5rem",
                                    color="#1F2937",
                                ),
                                rx.list(
                                    rx.el.li("30% improvement in fragmentation uniformity"),
                                    rx.el.li("50% reduction in flyrock incidents"),
                                    rx.el.li("15% increase in production efficiency"),
                                    list_style_type="disc",
                                    margin_bottom="1rem",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                rx.el.a(
                                    "Read Full Case Study",
                                    href="#",
                                    font_weight="600",
                                    _hover={"text-decoration": "underline"},
                                    color="#1D4ED8",
                                ),
                                background_color="#F3F4F6",
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                            ),
                            rx.box(
                                rx.heading(
                                    "Minimizing Vibration Impact",
                                    font_weight="700",
                                    margin_bottom="1.5rem",
                                    font_size="1.5rem",
                                    line_height="2rem",
                                    color="#1D4ED8",
                                    as_="h3",
                                ),
                                rx.flex(
                                    rx.image(
                                        alt="Before: High vibration levels causing community complaints",
                                        src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/FkpW7gpErvoLDd6bJfKric0fpfdWL5CSsLwGHWXDJZTqtgCnA/out-0.webp",
                                        height="12rem",
                                        object_fit="cover",
                                        border_radius="0.5rem",
                                        width="50%",
                                    ),
                                    rx.image(
                                        alt="After: Reduced vibrations and improved community relations",
                                        src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/2yg1iv9BfekYSk8dYI66reTTnI9fyNAf1VlxRYHhd8Sp2CKcC/out-0.webp",
                                        height="12rem",
                                        object_fit="cover",
                                        border_radius="0.5rem",
                                        width="50%",
                                    ),
                                    display="flex",
                                    margin_bottom="1.5rem",
                                    column_gap="1rem",
                                ),
                                rx.text(
                                    rx.text.strong("Client:", color="#1F2937"),
                                    " Urban Development Corp",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    rx.text.strong("Challenge:", color="#1F2937"),
                                    " Excessive vibrations affecting nearby residential areas",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    rx.text.strong("Solution:", color="#1F2937"),
                                    " Deployed advanced seismographs and customized energy distribution models",
                                    margin_bottom="0.5rem",
                                    color="#4B5563",
                                ),
                                rx.text(
                                    "Results:",
                                    font_weight="600",
                                    margin_bottom="0.5rem",
                                    color="#1F2937",
                                ),
                                rx.list(
                                    rx.el.li("40% reduction in peak particle velocity"),
                                    rx.el.li("75% decrease in community complaints"),
                                    rx.el.li(
                                        "Maintained productivity while adhering to stricter vibration limits"
                                    ),
                                    list_style_type="disc",
                                    margin_bottom="1rem",
                                    padding_left="1.25rem",
                                    color="#4B5563",
                                ),
                                rx.el.a(
                                    "Read Full Case Study",
                                    href="#",
                                    font_weight="600",
                                    _hover={"text-decoration": "underline"},
                                    color="#1D4ED8",
                                ),
                                background_color="#F3F4F6",
                                padding="2rem",
                                border_radius="0.75rem",
                                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                            ),
                            gap="2.5rem",
                            display="grid",
                            grid_template_columns=rx.breakpoints(
                                {
                                    "0px": "repeat(1, minmax(0, 1fr))",
                                    "768px": "repeat(2, minmax(0, 1fr))",
                                }
                            ),
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                    ),
                    id="case-studies",
                    background_color="#ffffff",
                    padding_top="5rem",
                    padding_bottom="5rem",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Latest Industry Insights",
                            font_weight="700",
                            margin_bottom="4rem",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color="#1D4ED8",
                            text_align="center",
                            as_="h2",
                        ),
                        rx.box(
                            rx.box(
                                rx.image(
                                    alt="Machine learning algorithms analyzing blast data",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/oNQtJf8m3NyAWa0j9VA8O9SatvTG219l1ePWuJiIGWr1WQhTA/out-0.webp",
                                    height="12rem",
                                    margin_bottom="1rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "The Future of AI in Blast Optimization",
                                    font_weight="700",
                                    margin_bottom="0.5rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Exploring how machine learning is revolutionizing blast design and execution in the mining industry.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.el.a(
                                    "Read More",
                                    href="#",
                                    font_weight="600",
                                    _hover={"text-decoration": "underline"},
                                    color="#1D4ED8",
                                ),
                                background_color="#ffffff",
                                padding="1.5rem",
                                border_radius="0.75rem",
                                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                            ),
                            rx.box(
                                rx.image(
                                    alt="Sustainable mining practices in action",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/ESCzr1BErirwLpvBu66nTQjVp4no1hYdYpw6XJFAdzfaLowJA/out-0.webp",
                                    height="12rem",
                                    margin_bottom="1rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Sustainable Blasting Techniques for the Modern Mine",
                                    font_weight="700",
                                    margin_bottom="0.5rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "Discover eco-friendly approaches to blasting that minimize environmental impact without sacrificing efficiency.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.el.a(
                                    "Read More",
                                    href="#",
                                    font_weight="600",
                                    _hover={"text-decoration": "underline"},
                                    color="#1D4ED8",
                                ),
                                background_color="#ffffff",
                                padding="1.5rem",
                                border_radius="0.75rem",
                                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                            ),
                            rx.box(
                                rx.image(
                                    alt="Advanced vibration monitoring equipment",
                                    src="https://reflex-hosting-dev-flexgen.s3.us-west-2.amazonaws.com/replicate/iWVflZu2TGRVSa4XNBAg91KNqKdZWiNfHFECf2oVkEoqtgCnA/out-0.webp",
                                    height="12rem",
                                    margin_bottom="1rem",
                                    object_fit="cover",
                                    border_radius="0.5rem",
                                    width="100%",
                                ),
                                rx.heading(
                                    "Next-Gen Vibration Monitoring: Beyond PPV",
                                    font_weight="700",
                                    margin_bottom="0.5rem",
                                    color="#1D4ED8",
                                    font_size="1.25rem",
                                    line_height="1.75rem",
                                    as_="h3",
                                ),
                                rx.text(
                                    "An in-depth look at cutting-edge vibration analysis techniques that go beyond traditional peak particle velocity measurements.",
                                    margin_bottom="1rem",
                                    color="#4B5563",
                                ),
                                rx.el.a(
                                    "Read More",
                                    href="#",
                                    font_weight="600",
                                    _hover={"text-decoration": "underline"},
                                    color="#1D4ED8",
                                ),
                                background_color="#ffffff",
                                padding="1.5rem",
                                border_radius="0.75rem",
                                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                            ),
                            gap="2.5rem",
                            display="grid",
                            grid_template_columns=rx.breakpoints(
                                {
                                    "0px": "repeat(1, minmax(0, 1fr))",
                                    "768px": "repeat(3, minmax(0, 1fr))",
                                }
                            ),
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                    ),
                    id="blog",
                    background_color="#F3F4F6",
                    padding_top="5rem",
                    padding_bottom="5rem",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Contact Us",
                            font_weight="700",
                            margin_bottom="4rem",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color="#1D4ED8",
                            text_align="center",
                            as_="h2",
                        ),
                        rx.flex(
                            rx.box(
                                rx.form(
                                    rx.box(
                                        rx.el.label(
                                            "Name",
                                            display="block",
                                            font_weight="600",
                                            margin_bottom="0.5rem",
                                            color="#374151",
                                        ),
                                        rx.el.input(
                                            id="name",
                                            name="name",
                                            required=True,
                                            type="text",
                                            border_width="1px",
                                            border_color="#D1D5DB",
                                            _focus={
                                                "outline-style": "none",
                                                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                                                "--ring-color": "#3B82F6",
                                            },
                                            padding_left="1rem",
                                            padding_right="1rem",
                                            padding_top="0.5rem",
                                            padding_bottom="0.5rem",
                                            border_radius="0.375rem",
                                            width="100%",
                                        ),
                                    ),
                                    rx.box(
                                        rx.el.label(
                                            "Email",
                                            display="block",
                                            font_weight="600",
                                            margin_bottom="0.5rem",
                                            color="#374151",
                                        ),
                                        rx.el.input(
                                            id="email",
                                            name="email",
                                            required=True,
                                            type="email",
                                            border_width="1px",
                                            border_color="#D1D5DB",
                                            _focus={
                                                "outline-style": "none",
                                                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                                                "--ring-color": "#3B82F6",
                                            },
                                            padding_left="1rem",
                                            padding_right="1rem",
                                            padding_top="0.5rem",
                                            padding_bottom="0.5rem",
                                            border_radius="0.375rem",
                                            width="100%",
                                        ),
                                    ),
                                    rx.box(
                                        rx.el.label(
                                            "Company",
                                            display="block",
                                            font_weight="600",
                                            margin_bottom="0.5rem",
                                            color="#374151",
                                        ),
                                        rx.el.input(
                                            id="company",
                                            name="company",
                                            type="text",
                                            border_width="1px",
                                            border_color="#D1D5DB",
                                            _focus={
                                                "outline-style": "none",
                                                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                                                "--ring-color": "#3B82F6",
                                            },
                                            padding_left="1rem",
                                            padding_right="1rem",
                                            padding_top="0.5rem",
                                            padding_bottom="0.5rem",
                                            border_radius="0.375rem",
                                            width="100%",
                                        ),
                                    ),
                                    rx.box(
                                        rx.el.label(
                                            "Service Interested In",
                                            display="block",
                                            font_weight="600",
                                            margin_bottom="0.5rem",
                                            color="#374151",
                                        ),
                                        rx.el.select(
                                            rx.el.option("Select a service", value=True),
                                            rx.el.option(
                                                "Precision Shot Measurement",
                                                value="precision-measurement",
                                            ),
                                            rx.el.option(
                                                "3D Projection and Modeling",
                                                value="3d-modeling",
                                            ),
                                            rx.el.option(
                                                "Blast Design Optimization",
                                                value="blast-optimization",
                                            ),
                                            rx.el.option(
                                                "Comprehensive Blasting Audits",
                                                value="auditing",
                                            ),
                                            id="service",
                                            name="service",
                                            border_width="1px",
                                            border_color="#D1D5DB",
                                            _focus={
                                                "outline-style": "none",
                                                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                                                "--ring-color": "#3B82F6",
                                            },
                                            padding_left="1rem",
                                            padding_right="1rem",
                                            padding_top="0.5rem",
                                            padding_bottom="0.5rem",
                                            border_radius="0.375rem",
                                            width="100%",
                                        ),
                                    ),
                                    rx.box(
                                        rx.el.label(
                                            "Message",
                                            display="block",
                                            font_weight="600",
                                            margin_bottom="0.5rem",
                                            color="#374151",
                                        ),
                                        rx.el.textarea(
                                            id="message",
                                            name="message",
                                            required=True,
                                            rows="4",
                                            border_width="1px",
                                            border_color="#D1D5DB",
                                            _focus={
                                                "outline-style": "none",
                                                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                                                "--ring-color": "#3B82F6",
                                            },
                                            padding_left="1rem",
                                            padding_right="1rem",
                                            padding_top="0.5rem",
                                            padding_bottom="0.5rem",
                                            border_radius="0.375rem",
                                            width="100%",
                                        ),
                                    ),
                                    rx.el.button(
                                        "Send Message",
                                        type="submit",
                                        background_color="#1D4ED8",
                                        transition_duration="300ms",
                                        font_weight="600",
                                        _hover={"background-color": "#2563EB"},
                                        padding_left="1.5rem",
                                        padding_right="1.5rem",
                                        padding_top="0.75rem",
                                        padding_bottom="0.75rem",
                                        border_radius="0.375rem",
                                        color="#ffffff",
                                        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                                    ),
                                    display="flex",
                                    flex_direction="column",
                                    gap="1.5rem",
                                ),
                                margin_bottom=rx.breakpoints(
                                    {"0px": "2.5rem", "1024px": "0"}
                                ),
                                padding_right=rx.breakpoints({"1024px": "2.5rem"}),
                                width=rx.breakpoints({"1024px": "50%"}),
                            ),
                            rx.box(
                                rx.heading(
                                    "Company Information",
                                    font_weight="700",
                                    margin_bottom="1.5rem",
                                    font_size="1.5rem",
                                    line_height="2rem",
                                    color="#1D4ED8",
                                    as_="h3",
                                ),
                                rx.box(
                                    rx.text(
                                        rx.icon(
                                            alt="Location icon",
                                            tag="map-pin",
                                            height="1.5rem",
                                            margin_right="0.75rem",
                                            width="1.5rem",
                                        ),
                                        " 123 Mining Avenue, Quarry City, RC 12345 ",
                                        display="flex",
                                        align_items="center",
                                        color="#4B5563",
                                    ),
                                    rx.text(
                                        rx.icon(
                                            alt="Phone icon",
                                            tag="phone",
                                            height="1.5rem",
                                            margin_right="0.75rem",
                                            width="1.5rem",
                                        ),
                                        " +1 (555) 123-4567 ",
                                        display="flex",
                                        align_items="center",
                                        color="#4B5563",
                                    ),
                                    rx.text(
                                        rx.icon(
                                            alt="Email icon",
                                            tag="mail",
                                            height="1.5rem",
                                            margin_right="0.75rem",
                                            width="1.5rem",
                                        ),
                                        " info@datablastconsulting.com ",
                                        display="flex",
                                        align_items="center",
                                        color="#4B5563",
                                    ),
                                    display="flex",
                                    flex_direction="column",
                                    gap="1rem",
                                ),
                                rx.box(
                                    rx.heading(
                                        "Follow Us",
                                        font_weight="700",
                                        margin_bottom="1rem",
                                        color="#1D4ED8",
                                        font_size="1.125rem",
                                        line_height="1.75rem",
                                        as_="h4",
                                    ),
                                    rx.flex(
                                        rx.el.a(
                                            rx.icon(
                                                alt="LinkedIn icon",
                                                tag="linkedin",
                                                height="2rem",
                                                width="2rem",
                                            ),
                                            href="#",
                                            transition_duration="300ms",
                                            _hover={"color": "#1D4ED8"},
                                            color="#4B5563",
                                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                                        ),
                                        rx.el.a(
                                            rx.icon(
                                                alt="Twitter icon",
                                                tag="twitter",
                                                height="2rem",
                                                width="2rem",
                                            ),
                                            href="#",
                                            transition_duration="300ms",
                                            _hover={"color": "#1D4ED8"},
                                            color="#4B5563",
                                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                                        ),
                                        rx.el.a(
                                            rx.icon(
                                                alt="Facebook icon",
                                                tag="facebook",
                                                height="2rem",
                                                width="2rem",
                                            ),
                                            href="#",
                                            transition_duration="300ms",
                                            _hover={"color": "#1D4ED8"},
                                            color="#4B5563",
                                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                                        ),
                                        display="flex",
                                        column_gap="1rem",
                                    ),
                                    margin_top="2.5rem",
                                ),
                                padding_left=rx.breakpoints({"1024px": "2.5rem"}),
                                width=rx.breakpoints({"1024px": "50%"}),
                            ),
                            display="flex",
                            flex_direction=rx.breakpoints(
                                {"0px": "column", "1024px": "row"}
                            ),
                        ),
                        width="100%",
                        style=rx.breakpoints(
                            {
                                "640px": {"max-width": "640px"},
                                "768px": {"max-width": "768px"},
                                "1024px": {"max-width": "1024px"},
                                "1280px": {"max-width": "1280px"},
                                "1536px": {"max-width": "1536px"},
                            }
                        ),
                        margin_left="auto",
                        margin_right="auto",
                        padding_left=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                        padding_right=rx.breakpoints(
                            {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                        ),
                    ),
                    id="contact",
                    background_color="#ffffff",
                    padding_top="5rem",
                    padding_bottom="5rem",
                ),
                padding_top="4rem",
            ),
            rx.box(
                rx.box(
                    rx.text(
                        "\u00a9 2023 DataBlast Consulting. All rights reserved.",
                        margin_bottom="1rem",
                    ),
                    rx.flex(
                        rx.el.a(
                            "Privacy Policy",
                            href="#",
                            transition_duration="300ms",
                            _hover={"color": "#60A5FA"},
                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        rx.el.a(
                            "Terms of Service",
                            href="#",
                            transition_duration="300ms",
                            _hover={"color": "#60A5FA"},
                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        rx.el.a(
                            "Sitemap",
                            href="#",
                            transition_duration="300ms",
                            _hover={"color": "#60A5FA"},
                            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
                            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
                        ),
                        display="flex",
                        justify_content="center",
                        column_gap="1rem",
                    ),
                    width="100%",
                    style=rx.breakpoints(
                        {
                            "640px": {"max-width": "640px"},
                            "768px": {"max-width": "768px"},
                            "1024px": {"max-width": "1024px"},
                            "1280px": {"max-width": "1280px"},
                            "1536px": {"max-width": "1536px"},
                        }
                    ),
                    margin_left="auto",
                    margin_right="auto",
                    padding_left=rx.breakpoints(
                        {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                    ),
                    padding_right=rx.breakpoints(
                        {"0px": "1rem", "640px": "1.5rem", "1024px": "2rem"}
                    ),
                    text_align="center",
                ),
                background_color="#1F2937",
                padding_top="2.5rem",
                padding_bottom="2.5rem",
                color="#ffffff",
            ),
            class_name="font-['Inter']",
            background_color="#F9FAFB",
            color="#1F2937",
        ),
    )


app = rx.App()
app.add_page(index)

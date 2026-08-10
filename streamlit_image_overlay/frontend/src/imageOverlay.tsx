import { FC, useRef, useState, useEffect, useLayoutEffect } from "react"
import type { FrontendRendererArgs } from "@streamlit/component-v2-lib"

import type { 
    Overlay, OverlayData, OverlayState, TooltipPosition,
    tooltipStyle, viewportStyle
 } from "./types"



export type ImageOverlayProps =
    Pick<
        FrontendRendererArgs<OverlayState, OverlayData>,
        "setStateValue" | "setTriggerValue"
    > & OverlayData


//// Function
function calculateTooltipPosition(
    x: number,
    y: number,
    popupWidth: number,
    popupHeight: number,
    containerWidth: number,
    containerHeight: number,
    offset = 10
): TooltipPosition {
    let left = x + offset
    let top = y + offset

    if (left + popupWidth > containerWidth)
        left = x - popupWidth - offset
    if (left < offset)
        left = offset

    if (top + popupHeight > containerHeight)
        top = y - popupHeight - offset
    if (top < offset)
        top = offset

    return {
        x: left,
        y: top
    }
}

//// Main
const ImageOverlay: FC<ImageOverlayProps> = (props) => {
    const {
        image,
        overlays,
        styles,
    } = props
    
    // Refs
    const viewportRef = useRef<HTMLDivElement>(null)
    const svgRef = useRef<SVGSVGElement>(null)
    const tooltipRef = useRef<HTMLDivElement>(null)


    // Tooltip
    const [selectedOverlay, setSelectedOverlay] = useState<Overlay | null>(null);
    const [tooltipPosition, setTooltipPosition] = useState<TooltipPosition>({ x: 0, y: 0 })
    const [pointerPosition, setPointerPosition] = useState<TooltipPosition>({ x: 0, y: 0 })

    function handleOverlayEnter(
        event: React.PointerEvent<SVGElement>,
        overlay: Overlay
    ) {
        if (!svgRef.current)
            return

        const container = viewportRef.current!.getBoundingClientRect()

        setSelectedOverlay(overlay)

        setPointerPosition({
            x: event.clientX - container.left,
            y: event.clientY - container.top
        })
    }

    function hideTooltip() {
        setSelectedOverlay(null)
    }

    
    // View & overlay
    const [viewBox, setViewBox] = useState({
        x: 0,
        y: 0,
        width: 100,
        height: 100
    })

    function renderOverlay(overlay: Overlay) {
        switch (overlay.type) {
            case "circle":
                return (
                    <circle
                        key = {overlay.id}
                        cx = {overlay.data.x}
                        cy = {overlay.data.y}
                        r = {overlay.data.radius}
                        style = {{
                            fill: "rgba(255, 255, 255, 0)",
                            stroke: "white",
                            strokeWidth: 1,
                            ...styles.circle,
                        }}
                        onPointerEnter = {(event) =>
                            handleOverlayEnter(event, overlay)
                        }
                        onPointerLeave = {hideTooltip}
                    />
                )
            default:
                return null
        }
    }

    function fitToWindow() {
        setViewBox({
            x: 0,
            y: 0,
            width: image.width,
            height: image.height
        })
    }

    function panBy(dx: number, dy: number) {
        const viewport = viewportRef.current

        if (!viewport)
            return

        setViewBox(prev => ({
            ...prev,
            x: prev.x - dx * prev.width / viewport.clientWidth,
            y: prev.y - dy * prev.height / viewport.clientHeight
        }))
    }

    function zoomAt(
        mouseX: number,
        mouseY: number,
        factor: number,
        rWidth: number,
        rHeight: number
    ) {
        setViewBox(prev => {
            const imageX = prev.x + mouseX * prev.width / rWidth
            const imageY = prev.y + mouseY * prev.height / rHeight
            const width = prev.width * factor
            const height = prev.height * factor
            return {
                x: imageX - mouseX * width / rWidth,
                y: imageY - mouseY * height / rHeight,
                width,
                height
            }
        })
    }


    // Mouse interaction
    const [isDragging, setIsDragging] = useState(false)

    const [lastMouse, setLastMouse] = useState({
        x: 0,
        y: 0
    })

    const handleWheel = (event: React.WheelEvent) => {
        event.preventDefault()
        const rect = viewportRef.current!.getBoundingClientRect()
        const mouseX = event.clientX - rect.left
        const mouseY = event.clientY - rect.top
        const scaleFactor = event.deltaY < 0 ? 1 / 1.1 : 1.1
        zoomAt(mouseX, mouseY, scaleFactor, rect.width, rect.height)
    }

    const handleMouseDown = (event: React.MouseEvent) => {
        setIsDragging(true)
        setLastMouse({
            x: event.clientX,
            y: event.clientY
        })
    }

    const handleMouseMove = (event: React.MouseEvent) => {
        if (!isDragging)
            return

        panBy(event.clientX - lastMouse.x, event.clientY - lastMouse.y)
        setLastMouse({
            x: event.clientX,
            y: event.clientY
        })
    }

    const handleMouseUp = () => {
        setIsDragging(false)
    }


    // Initialize view when a new image is loaded
    useEffect(() => {
        fitToWindow()
    }, [image.src, image.width, image.height])


    // Update tooltip position
    useLayoutEffect(() => {
        if (
            !selectedOverlay ||
            !tooltipRef.current ||
            !svgRef.current
        )
            return

        const tooltip = tooltipRef.current.getBoundingClientRect()
        const container = svgRef.current.parentElement!.getBoundingClientRect()

        setTooltipPosition(
            calculateTooltipPosition(
                pointerPosition.x,
                pointerPosition.y,
                tooltip.width,
                tooltip.height,
                container.width,
                container.height
            )
        )

    }, [selectedOverlay, pointerPosition])


    return (
        <div
            ref = {viewportRef}
            style = {{
                ...viewportStyle,
                ...styles.viewport,
            }}

            onWheel = {handleWheel}
            onMouseDown = {handleMouseDown}
            onMouseMove = {handleMouseMove}
            onMouseUp = {handleMouseUp}
            onMouseLeave = {handleMouseUp}
            onDoubleClick = {fitToWindow}
        >
            <svg
                ref = {svgRef}
                viewBox = {`${viewBox.x} ${viewBox.y} ${viewBox.width} ${viewBox.height}`}
                preserveAspectRatio = "xMidYMid meet"
                style = {{                    
                    display: "block",
                    width: "100%",
                    height: "100%"
                }}
            >
                <image
                    href = {image.src}
                    x = {0}
                    y = {0}
                    width = {image.width}
                    height = {image.height}
                />

                {overlays.map(renderOverlay)}
            </svg>

            {selectedOverlay && (
                <div
                    ref = {tooltipRef}
                    style = {{
                        ...tooltipStyle,
                        ...styles.tooltip,
                        left: tooltipPosition.x,
                        top: tooltipPosition.y,
                    }}
                >
                    {selectedOverlay.tooltip}
                </div>
            )}
        </div>
    )
}

export default ImageOverlay
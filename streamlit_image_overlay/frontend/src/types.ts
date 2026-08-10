import type { FrontendState } from "@streamlit/component-v2-lib";
import type { CSSProperties } from "react";


export interface CircleOverlay {
    id: string;
    type: "circle";
    data: {
        x: number;
        y: number;
        radius: number;
    };
    tooltip: string;
}


export type Overlay = CircleOverlay;


export interface TooltipPosition {
    x: number;
    y: number;
}


export interface OverlayState extends FrontendState {
}


export interface OverlayData {
    image: string;
    imageWidth: number;
    imageHeight: number;
    overlays: Overlay[];
    styles: ComponentStyles;
}

export interface ComponentStyles {
    circle?: CSSProperties;
    //contour?: CSSProperties;
    tooltip?: CSSProperties;
    viewport?: CSSProperties;
    image?: CSSProperties;
}
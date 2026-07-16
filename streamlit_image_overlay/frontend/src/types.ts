import type { FrontendState } from "@streamlit/component-v2-lib";

export interface Particle {
    id: number;
    x: number;
    y: number;
    diameter: number;
    projectionArea: number;
    volume: number;
    c0: number;
    approxError: number;
}


export interface TooltipPosition {
    x: number;
    y: number;
}


export interface OverlayMetadata {
    unit: string;
}

export interface OverlayState extends FrontendState {

}

export interface OverlayData {
    image: string;
    imageWidth: number;
    imageHeight: number;
    particles: Particle[];
    metadata: OverlayMetadata;
}